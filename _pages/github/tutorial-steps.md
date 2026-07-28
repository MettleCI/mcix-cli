---
title: GitHub Pipeline Tutorial Steps
description: Implementing a simple CI/CD pipeline using MCIX GitHub Actions
tech: github
order: 4
---

## Scenario

This tutorial shows how to implement a simple CI/CD pipeline for DataStage NextGen using MCIX GitHub Actions.

Unlike the command-line tutorial, you won’t manually run each `mcix` command from your local shell. Instead, you’ll define a GitHub Actions workflow that executes the relevant MCIX actions on a GitHub Actions runner.

We’ll use GitHub Actions to create a pipeline ('workflow') which respond to a `git push` trigger. It will:

1. Check out your repository.
2. Verify the MCIX action version and capabilities.
3. Apply CI environment-specific [overlays](/introduction/overlays).
4. Import the overlaid DataStage assets into your CI project.
5. Compile the imported assets.
6. Execute DataStage unit tests.
7. Run asset analysis tests.
8. Upload generated JUnit reports as workflow artefacts.

It is assumed you already have:

- a GitHub repository containing exported DataStage assets
- a target DataStage NextGen project into which assets can be imported, compiled, and tested
- environment-specific overlay files stored in your repository
- unit-test specifications and associated test data for at least some DataStage flows
- asset-analysis rules available in your repository
- a GitHub Environment called `ci`
- GitHub variables and secrets configured for your DataStage connection details

## Constructing the pipeline

The pipeline we’ll build will run when changes are pushed to the `main` branch, or when you manually trigger it from the GitHub Actions user interface.

The pipeline will perform the following operations:

1. Check out the repository.
2. Create local output directories.
3. Verify the MCIX action runtime.
4. Deploy the DataStage assets to the CI project:
   - apply overlays
   - import assets
   - compile assets
5. Execute unit tests.
6. Run asset analysis tests.
7. Upload generated reports.

```mermaid
sequenceDiagram
    %%{init: {'sequence': {'diagramMarginY': 50, 'mirrorActors': false}}}%%

    actor Dev as Developer
    participant GitHub as GitHub<br/>Repository<br/><br/><br/><br/>
    participant Actions as GitHub Actions<br/>Runner<br/><br/><br/><br/>
    participant MCIX as MCIX<br/>Actions<br/><br/><br/><br/>
    participant DSCI as DataStage<br/>CI Project<br/><br/><br/><br/>

    Dev->>()GitHub: git push
    GitHub->>Actions: Trigger workflow
    activate Actions
      GitHub()->>Actions: Checkout repository
      Actions->>MCIX: system version
      activate MCIX
      MCIX->>Actions: MCIX information
      deactivate MCIX
      Actions->>MCIX: datastage deploy
      activate MCIX
        MCIX->>MCIX: overlay apply
        MCIX->>()DSCI: datastage import
        MCIX->>DSCI: datastage compile
      deactivate MCIX
      Actions->>MCIX: unit-test execute
      activate MCIX
        MCIX->>DSCI: Execute unit tests
      deactivate MCIX
      {% if site.compliance == "Y" %}
      Actions->>MCIX: asset-analysis test
      {% endif %}
      Actions->>GitHub: Upload JUnit reports
    deactivate Actions
```
The example assumes you are moving DataStage assets from source control into a CI project, applying environment-specific overlays, compiling the result, and then validating the deployed assets.

---

## 1. Prepare your repository

After completing the prerequisite steps, your repository should look something like this:

```text
mcix-github-actions-demo/
├── .github/
│   └── workflows/
│       └── mcix-ci.yaml
├── datastage/
│   └── <exported DataStage assets>
├── filesystem/
│   └── <non-DataStage files>
├── overlays/
│   └── ci/
└── README.md
```

Of particular note are these directories:

| Directory               | Purpose                                                |
| :---------------------- | :----------------------------------------------------- |
| `datastage/`            | Stores exported DataStage assets under version control |
| `overlays/`             | Stores environment-specific overlay files              |
| `.github/workflows/`    | Stores GitHub Actions workflow definitions             |

The GitHub Actions workflow will run from the root of the repository, so all file paths in the workflow should be relative to the repository root.

---

## 2. Confirm your GitHub Environment values

This tutorial assumes you created a GitHub Environment called `ci`.

In your repository, navigate to:<br/>
**Settings** → **Environments** → **ci**

Confirm the following variables exist:

| Variable            | Example value             | Description                           |
| :------------------ | :------------------------ | :------------------------------------ |
| `CP4D_URL`          | `https://cpd.example.com` | Base URL of your DataStage service    |
| `CP4D_USER`         | `my-user@example.com`     | Username used to connect to DataStage |
| `DATASTAGE_PROJECT` | `mcix-demo_ci`            | Target CI DataStage project           |

Confirm the following secret exists:

| Secret         | Description                               |
| :------------- | :---------------------------------------- |
| `CP4D_API_KEY` | API key used to authenticate to DataStage |

The workflow examples below use these values via GitHub’s `vars` and `secrets` contexts:

```yaml
{% raw %}${{ vars.CP4D_URL }}
${{ vars.CP4D_USER }}
${{ vars.DATASTAGE_PROJECT }}
${{ secrets.CP4D_API_KEY }}{% endraw %}
```

Using GitHub Environment values keeps your workflow portable. The same workflow can later be reused 
for `qa` or `prod`, simply by changing the job’s target environment.

---

## 3. Create the initial workflow file

We'll augment the simple validation workflow you created during the [prerequisites](/github/tutorial-prerequisites) step. Open the `.yaml` file you created:

```text
.github/workflows/mcix-ci.yaml
```

This workflow will run whenever changes are pushed to `main`, and can also be run manually from the GitHub Actions user interface.

Start with this structure:

```yaml
name: MCIX CI Pipeline                # The name of the workflow

on:                                   # Tell GitHub to trigger this pipeline whenever
  push:                               # a push is made to the repository's `main` branch
    branches:                         #
      - main                          #

  workflow_dispatch:                  # Allows this workflow to be run manually with
                                      # a Run workflow button in the GitHub Actions tab

jobs:                                 # Define a job with 
  deploy-ci:                          # a reference, and 
    name: Deploy to CI                # a name.

    runs-on: ubuntu-latest            # Run this Job on the latest Ubuntu image on GitHub infrastrcuture.

    environment: ci                   # Bind the Job to your `ci` GitHub Environment, making 
                                      # that environment’s variables and secrets available to the job. 

    permissions:                      # Grants the workflow read access to the repository contents. 
      contents: read                  # That is sufficient for most needs as the workflow reads files and 
                                      # runs actions but does not normally need to write to the repository.

    steps:                            # The operations perfomed by this Job.
      - name: Checkout repository
        uses: actions/checkout@v6
```

---

## 4. Verify the MCIX runtime

Before running a full deployment, add a simple MCIX System Version step.

```yaml
      - name: Verify MCIX runtime
        uses: MettleCI/mcix-system-version@v0
```

This step confirms that the GitHub runner can execute the MCIX action successfully.

At this point your workflow should look like this:

```yaml
name: MCIX CI Workflow

on:
  push:
    branches:
      - main

  workflow_dispatch:

jobs:
  deploy-ci:
    name: Deploy to CI
    runs-on: ubuntu-latest
    environment: ci

    permissions:
      contents: read

    steps:
      - name: Checkout repository         
        uses: actions/checkout@v6

      - name: Verify MCIX runtime
        uses: MettleCI/mcix-system-version@v0
```

Commit and push the workflow:

```bash
git add .github/workflows/mcix-ci.yaml
git commit -m "Add MCIX CI workflow"
git push
```

Then open your repository in GitHub and navigate to:<br/>
**Actions** → **MCIX CI Pipeline**

A successful run confirms that GitHub Actions can start the workflow and execute an MCIX action.

---

## 6. Add the DataStage deployment step

Now you'll add the main deployment step.  This tutorial uses the [MCIX DataStage Deploy](/github/action-reference#datastage-deploy) action, 
which performs the common deployment sequence:

```text
overlay apply → datastage import → datastage compile
```

Add this step after `Verify MCIX runtime`:

```yaml
{% raw %}      - name: Deploy DataStage assets
        id: deploy
        uses: MettleCI/mcix-composite-deploy@v0
        with:
          api-key: ${{ secrets.CP4D_API_KEY }}
          url: ${{ vars.CP4D_URL }}
          user: ${{ vars.CP4D_USER }}
          project: ${{ vars.DATASTAGE_PROJECT }}

          assets: datastage
          overlays: overlays/ci
          output: build/ci-assets.zip

          import-report: reports/import-report.xml
          compile-report: reports/compile-report.xml{% endraw %}
```

This step:

1. Reads the exported assets from `datastage`.
2. Applies the overlays in `overlays/ci`.
3. Writes the overlaid assets to `build/ci-assets.zip`.
4. Imports the overlaid assets into the CI DataStage project.
5. Compiles the imported assets.
6. Writes import and compile reports to the `reports` directory.

If you prefer to identify the DataStage project by ID rather than by name, replace:

```yaml
{% raw %}          project: ${{ vars.DATASTAGE_PROJECT }}{% endraw %}
```

with:

```yaml
{% raw %}          project-id: ${{ vars.DATASTAGE_PROJECT_ID }}{% endraw %}
```

Do not supply both `project` and `project-id`.

---

## 7. Run unit tests

After deployment, execute the DataStage unit tests in the CI project.

Add this step after the deployment step:

```yaml
{% raw %}      - name: Execute DataStage unit tests
        id: unit-tests
        uses: MettleCI/mcix-unit-test-execute@v0
        with:
          api-key: ${{ secrets.CP4D_API_KEY }}
          url: ${{ vars.CP4D_URL }}
          user: ${{ vars.CP4D_USER }}
          project: ${{ vars.DATASTAGE_PROJECT }}
          report: reports/unit-test-report.xml
          test-suite: mcix ci tests
          max-concurrency: 8{% endraw %}
```

This step runs unit tests against the deployed assets in your target CI project and writes a JUnit-style report file to:

```text
reports/unit-test-report.xml
```

The `max-concurrency` value controls the number of unit test jobs that can be executed concurrently.

For an introductory tutorial, `8` is a reasonable starting value. In a real environment, tune this value based on the capacity of your DataStage environment.

---

## 8. Run asset analysis tests

Next, run asset analysis tests against the DataStage assets.

Add this step after the unit test step:

```yaml
{% raw %}      - name: Run asset analysis tests
        id: asset-analysis
        uses: MettleCI/mcix-asset-analysis-test@v0
        with:
          api-key: ${{ secrets.CP4D_API_KEY }}
          url: ${{ vars.CP4D_URL }}
          user: ${{ vars.CP4D_USER }}
          project: ${{ vars.DATASTAGE_PROJECT }}
          path: datastage
          rules: asset-analysis-rules
          report: reports/asset-analysis-report.xml
          test-suite: mcix asset analysis{% endraw %}
```

This step writes its JUnit-style report to:

```text
reports/asset-analysis-report.xml
```

The `path` input points to the assets being analysed. For this tutorial, we’ll analyse the source-controlled DataStage assets in the `datastage` directory.

---

## 9. Upload generated reports

Finally, upload the generated reports as GitHub Actions artefacts.

Add this step at the end of the job:

```yaml
      - name: Upload MCIX reports
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: mcix-reports
          path: reports/
```

The `if: always()` condition ensures that reports are uploaded even if an earlier validation or test step fails.

This is useful because the report files often contain the details you need to diagnose the failure.

---

## 10. Review the completed workflow

Your completed workflow should now look like this:

```yaml
{% raw %}name: MCIX CI Pipeline

on:
  push:
    branches:
      - main

  workflow_dispatch:

jobs:
  deploy-ci:
    name: Deploy to CI
    runs-on: ubuntu-latest
    environment: ci

    permissions:
      contents: read

    steps:
      - name: Checkout repository
        uses: actions/checkout@v6

      - name: Prepare output directories
        run: |
          mkdir -p build
          mkdir -p reports

      - name: Verify MCIX runtime
        uses: MettleCI/mcix-system-version@v0

      - name: Deploy DataStage assets
        id: deploy
        uses: MettleCI/mcix-composite-deploy@v0
        with:
          api-key: ${{ secrets.CP4D_API_KEY }}
          url: ${{ vars.CP4D_URL }}
          user: ${{ vars.CP4D_USER }}
          project: ${{ vars.DATASTAGE_PROJECT }}

          assets: datastage
          overlays: overlays/ci
          output: build/ci-assets.zip

          import-report: reports/import-report.xml
          compile-report: reports/compile-report.xml

      - name: Execute DataStage unit tests
        id: unit-tests
        uses: MettleCI/mcix-unit-test-execute@v0
        with:
          api-key: ${{ secrets.CP4D_API_KEY }}
          url: ${{ vars.CP4D_URL }}
          user: ${{ vars.CP4D_USER }}
          project: ${{ vars.DATASTAGE_PROJECT }}
          report: reports/unit-test-report.xml
          test-suite: mcix ci tests
          max-concurrency: 8

      - name: Run asset analysis tests
        id: asset-analysis
        uses: MettleCI/mcix-asset-analysis-test@v0
        with:
          api-key: ${{ secrets.CP4D_API_KEY }}
          url: ${{ vars.CP4D_URL }}
          user: ${{ vars.CP4D_USER }}
          project: ${{ vars.DATASTAGE_PROJECT }}
          path: datastage
          rules: asset-analysis-rules
          report: reports/asset-analysis-report.xml
          test-suite: mcix asset analysis

      - name: Upload MCIX reports
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: mcix-reports
          path: reports/{% endraw %}
```

Commit and push the updated workflow:

```bash
git add .github/workflows/mcix-ci.yaml
git commit -m "Add MCIX deployment and test pipeline"
git push
```

GitHub will automatically start the workflow because the workflow is configured to run on pushes to `main`.

---

## 11. Run the pipeline manually

You can also run the workflow manually.

In GitHub, navigate to:<br/>
**Actions** → **MCIX CI Pipeline** → **Run workflow**

Choose the `main` branch and click:<br/>
**Run workflow**

GitHub will create a new workflow run and execute the MCIX pipeline against the `ci` environment.

---

## 12. Review the workflow output

When the workflow completes, open the workflow run in GitHub.

Review each step:

| Step                           | Expected result                                   |
| :----------------------------- | :------------------------------------------------ |
| `Checkout repository`          | Repository contents are available to the workflow |
| `Verify MCIX runtime`          | MCIX runtime starts successfully                  |
| `Deploy DataStage assets`      | Assets are overlaid, imported, and compiled       |
| `Execute DataStage unit tests` | Unit tests are executed in the CI project         |
| `Run asset analysis tests`     | Asset-analysis rules are applied                  |
| `Upload MCIX reports`          | Generated XML reports are uploaded                |

The workflow should produce a downloadable artefact called:

```text
mcix-reports
```

This artefact should contain files similar to:

```text
reports/
├── import-report.xml
├── compile-report.xml
├── unit-test-report.xml
└── asset-analysis-report.xml
```

---

## 13. Make a development change

Next, make a trivial change to one of your DataStage flows in your source DataStage project.

For example:

1. Open your source DataStage project.
2. Open a DataStage flow.
3. Modify a description field or another non-functional property.
4. Save the flow.

Then export the updated assets into your local repository using your normal development process.

This may be done using:

* the MCIX CLI,
* a MettleCI Workbench-based process,
* an existing export process, or
* another project-specific process used by your team.

After the export, inspect the repository changes:

```bash
git status
```

Stage the relevant changed asset files:

```bash
git add datastage/data_intg_flow/<YourChangedFlow>.json
```

Commit and push the change:

```bash
git commit -m "Update tutorial DataStage flow"
git push
```

The push to `main` will trigger the GitHub Actions pipeline.

---

## 14. Confirm the pipeline redeploys the change

Open the new workflow run in GitHub:<br/>
**Actions** → **MCIX CI Pipeline**

Confirm that the pipeline has:

1. Checked out the updated repository contents.
2. Applied CI overlays.
3. Imported the updated DataStage assets into the CI project.
4. Compiled the CI project.
5. Executed unit tests.
6. Run asset analysis tests.
7. Uploaded reports.

You can also open the target CI DataStage project and confirm that the changed flow has been updated there.

---

## 15. Optional: Use individual actions instead of the deploy action

The [MCIX DataStage Deploy](/github/action-reference#datastage-deploy) action is a convenient shortcut for this common sequence:

```text
overlay apply → datastage import → datastage compile
```

If you prefer to show each stage individually in the tutorial, replace the single deployment step with these three explicit steps.

```yaml
{% raw %}      - name: Apply CI overlays
        id: overlay
        uses: MettleCI/mcix-overlay-apply@v0
        with:
          assets: datastage
          overlays: overlays/ci
          output: build/ci-assets.zip

      - name: Import DataStage assets
        id: import
        uses: MettleCI/mcix-datastage-import@v0
        with:
          api-key: ${{ secrets.CP4D_API_KEY }}
          url: ${{ vars.CP4D_URL }}
          user: ${{ vars.CP4D_USER }}
          project: ${{ vars.DATASTAGE_PROJECT }}
          assets: build/ci-assets.zip
          report: reports/import-report.xml

      - name: Compile DataStage assets
        id: compile
        uses: MettleCI/mcix-datastage-compile@v0
        with:
          api-key: ${{ secrets.CP4D_API_KEY }}
          url: ${{ vars.CP4D_URL }}
          user: ${{ vars.CP4D_USER }}
          project: ${{ vars.DATASTAGE_PROJECT }}
          report: reports/compile-report.xml{% endraw %}
```

This is more verbose, but it makes the pipeline mechanics clearer for users who are learning how the MCIX operations relate to one another.

For the main tutorial, however, the composite deployment action is simpler and closer to what most users will want in a real GitHub Actions pipeline.

---

## Expected results

After the workflow completes successfully, you should have:

```text
mcix-github-actions-demo/
├── datastage/
│   └── source-controlled DataStage assets
├── overlays/
│   └── ci/
├── build/
│   └── ci-assets.zip
└── reports/
    ├── import-report.xml
    ├── compile-report.xml
    ├── unit-test-report.xml
    └── asset-analysis-report.xml
```

The generated `build/` and `reports/` directories exist only inside the workflow run unless you create them locally or upload them as artefacts.

The pipeline has:

1. Retrieved DataStage assets from source control.
2. Applied CI-specific overlays.
3. Imported the transformed assets into the CI DataStage project.
4. Compiled the deployed assets.
5. Executed DataStage unit tests.
6. Applied asset-analysis rules.
7. Published generated reports as workflow artefacts.

---

## Notes for real-world usage

For a production-quality workflow, consider the following refinements:

* Use separate GitHub Environments for `ci`, `qa`, and `prod`.
* Add deployment approval rules to protected environments.
* Pin MCIX actions to specific versions rather than broad major versions.
* Run CI deployments from feature branches or pull requests before merging to `main`.
* Keep secrets in GitHub Secrets, not in workflow YAML.
* Keep environment-specific values in GitHub Environment variables.
* Do not commit generated `build/` or `reports/` output to source control.
* Use branch protection rules once the tutorial workflow is working.
* Consider splitting validation and deployment into separate jobs if your real pipeline requires approvals or promotion gates.
