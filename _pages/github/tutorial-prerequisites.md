---
title: GitHub Pipeline Tutorial Prerequisites
description: Establishing the conditions for a pipeline using MCIX GitHub Actions
---

Before you begin this tutorial you’ll need to prepare your DataStage projects, GitHub repository, GitHub Actions environment configuration, and the credentials required to connect GitHub Actions to your DataStage service.

<cds-inline-notification
  kind="warning"
  title="Important"
  low-contrast
  hide-close-button="true"
  id="overlay-notification">
  <div>
  Ideally, this tutorial would not require you to install the MCIX CLI on your local host as there would be a suitable direct interface between the DataStage user interface and your Git platform. However, due to the requirement for the <a href="/notes/git-interface">interim Git Interface</a>, you should start this tutorial by following the <a href="/command-line/tutorial-prerequisites#install-the-mcix-command-line">Install the MCIX command line</a> section of the Command Line tutorial.
  </div>
</cds-inline-notification>

---

## Configure your DataStage projects

Ensure you have a DataStage NextGen project for each of the environments you use during the tutorial:

1. Your source `Development` environment, and
2. Each environment to which you wish to deploy.

For the purposes of this tutorial we’ll use a single CI target environment.

| Environment | Project name |
| :---        | :--- |
| Development | `mcix-demo` |
| CI          | `mcix-demo_ci` |

Ensure your DataStage NextGen projects are not configured as Git integrated projects.

- Do not select **Git Integrated** when creating the project.
- Do not select **Enable Git integration** in the settings of the created project.

In this tutorial GitHub is the source of truth for your DataStage assets. DataStage projects represent environment-specific deployments of that source.

## Generate an API key

If you don’t yet have one, generate an API key for the user account that GitHub Actions will use to connect to DataStage.

The type of key you need to generate depends on whether you are using DataStage NextGen on a self-hosted platform or IBM Cloud-hosted DataStage-as-a-Service.

#### Self-hosted

Create an API key using IBM’s guidance for your platform. Depending on your IBM Software Hub / Cloud Pak configuration, this may be either:

- a platform API key, or
- an instance API key.

#### SaaS

For IBM Cloud-hosted DataStage-as-a-Service, create an **IBM Cloud API key**, not a Cloud Pak API key.

Note that the value of an IBM Cloud API key is only available for download/copy at creation time. The copy icon shown next to an existing key copies the key ID, not the secret key value.

## Configure DataStage test data storage

As part of this tutorial you may execute unit tests against one or more DataStage flows.  To support this, configure test data storage in the DataStage project where tests will be executed. For this tutorial, that will normally be your CI project.  

If you want to use the sample project provided with this tutorial then ensure that your test data storage connection is called `TestDataConnection`.

## Prepare a GitHub repository

Before running a GitHub Actions-based MCIX pipeline, you need a GitHub repository containing your DataStage assets, overlays, workflow definitions, and any supporting files.

Use a simple, purpose-based repository name, such as:

```text
mcix-github-actions-demo
```

Avoid naming the repository after a specific environment, such as myproject-prod or myproject-test. The repository should represent the single source of truth for the DataStage initiative, not one particular deployment target.

Recommended settings for your repository:

| Setting           | Value                      |
| :---------------- | :------------------------- |
| Repository name   | `mcix-github-actions-demo` |
| Visibility        | Private                    |
| Default branch    | `main`                     |
| `.gitignore`      | Yes                        |
| README            | Yes                        |
| Licence           | Optional                   |
| Issues            | Disabled                   |
| Wiki              | Disabled                   |
| Discussions       | Disabled                   |
| Projects/Boards   | Disabled                   |
| Branch protection | Disabled for this tutorial |

You can enable branch protection, pull request review rules, and deployment approvals later. 
For this introductory tutorial, keep the repository simple so you can focus on the pipeline mechanics.

## Clone the MettleCI template repository

A MettleCI template repository is provided for convenience and as a recommended starting point.

You are not required to follow the template repository’s structure. You can organise your repository in 
whatever way best suits your project, including where you store DataStage assets, scripts, configuration 
files, documentation, and other non-DataStage artefacts.

The template repository does, however, demonstrate a practical best-practice layout that is easy to understand, 
easy to deploy, and suitable for most delivery pipelines.

Clone the template repository to your local host:

```shell
git clone https://github.com/MettleCI/datastage-nextgen-repo-template
```

Rename the local directory to match your new GitHub repository:

```shell
mv datastage-nextgen-repo-template mcix-github-actions-demo
cd mcix-github-actions-demo
```

Inspect the repository contents:

```shell
ls -al
```
You should see a structure similar to this:

```shell
mcix-github-actions-demo/
├── .git
├── .gitattributes
├── .gitignore
├── datastage/
├── filesystem/
├── overlays/
└── README.md
```

Now point the local clone to your new GitHub repository:

```shell
git remote set-url origin <YOUR_NEW_GITHUB_REPOSITORY_URL>
```
For example:

```shell
git remote set-url origin git@github.com:my-org/mcix-github-actions-demo.git
```
Push the template contents to your new repository:

```shell
git push -u origin main
```
You can now open your GitHub repository in a browser and confirm that the template files are visible.

## Enable GitHub Actions

GitHub Actions must be enabled for your repository.

In GitHub, navigate to: <br/>
**Repository** → **Settings** → **Actions** → **General**

For this tutorial, ensure that **Actions** are allowed to run in the repository.

If your organisation restricts which actions can be used, confirm that your repository is allowed to 
use the MettleCI MCIX actions from GitHub Marketplace.

The MCIX actions used in this tutorial are published by MettleCI and include:

| Action                              | Purpose                                                             |
| :---------------------------------- | :------------------------------------------------------------------ |
| `MettleCI/mcix-system-version`      | Verifies the MCIX runtime available to the action                   |
| `MettleCI/mcix-overlay-apply`       | Applies environment overlays to exported DataStage assets           |
| `MettleCI/mcix-datastage-import`    | Imports DataStage assets into a target project                      |
| `MettleCI/mcix-datastage-compile`   | Compiles DataStage assets in a target project                       |
| `MettleCI/mcix-asset-analysis-test` | Runs asset analysis rules                                           |
| `MettleCI/mcix-unit-test-execute`   | Executes MettleCI unit tests                                        |
| `MettleCI/mcix-composite-deploy`    | Performs overlay, import, and compile as a single deployment action |

## Confirm runner requirements

The MCIX GitHub Actions are designed to run in GitHub Actions workflows using Linux runners.

For this tutorial, use the GitHub-hosted Ubuntu runner:

```yaml
runs-on: ubuntu-latest
```

This avoids the need to configure your own self-hosted runner.

If you use a self-hosted runner instead, it must be a Linux runner capable of executing container-based 
GitHub Actions. It must also have network access to:

- your GitHub repository,
- the MCIX action repositories,
- the MCIX container image registry, and
- your DataStage service URL.

## Create GitHub environment configuration

This tutorial uses GitHub Environments to keep environment-specific configuration separate from the workflow logic.

Create a GitHub Environment for your CI deployment target: <br/>
**Repository** → **Settings** → **Environments** → **New environment**

Name the environment:

```text
ci
```

Then add the following environment variables:

| Variable            | Example value             | Description                           |
| :------------------ | :------------------------ | :------------------------------------ |
| `CP4D_URL`          | `https://cpd.example.com` | Base URL of your DataStage service    |
| `CP4D_USER`         | `my-user@example.com`     | Username used to connect to DataStage |
| `DATASTAGE_PROJECT` | `mcix-demo-ci`            | Target CI DataStage project name      |

Add the following environment secret:

| Secret         | Description                               |
| :------------- | :---------------------------------------- |
| `CP4D_API_KEY` | API key used to authenticate to DataStage |

Use variables for non-sensitive values such as URLs, usernames, and project names. Use secrets for 
sensitive values such as API keys.

## Check repository workflow permissions

In your repository, navigate to: <br/>
**Repository** → **Settings → **Actions** → **General** → **Workflow permissions**

For this tutorial, the default read permissions are usually sufficient because the workflow will read 
repository contents and execute MCIX actions.

If you later extend the workflow to create releases, write pull request comments, publish packages, or 
update repository contents, you may need to grant additional permissions explicitly in your workflow.

## Create the workflow directory

GitHub Actions workflow files are stored in the .github/workflows directory at the root of your repository.

Create that directory if it does not already exist:

```bash
mkdir -p .github/workflows
```
## Add a simple MCIX verification workflow

Before building the full pipeline, create a simple workflow that verifies your repository can execute an MCIX action.

Create this file which will create a simple workflow using the [MCIX system version](/github/action-reference#system-version) action:

```
.github/workflows/mcix-ci.yaml
```

Add the following content:

```yaml
name: MCIX CI Workflow

on:
  workflow_dispatch:

jobs:
  mcix-system-version:
    name: Verify MCIX runtime
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v6

      - name: Run MCIX System Version
        uses: MettleCI/mcix-system-version@v1
```

We'll run through the role of this file and meaning of each line in the [tutorial steps](tutorial-steps). For now, commit and push the workflow:

```shell
git add .github/workflows/mcix-ci.yaml
git commit -m "Add MCIX system version workflow"
git push
```

Then run the workflow manually:<br/>
**Repository** → **Actions** → **MCIX System Version** → **Run workflow**

A successful run confirms that:

- GitHub Actions is enabled for the repository,
- the repository can use the MCIX action,
- the speicfied runner (an `ubuntu-latest` instance dynamically provisioned by GitHub, in this instance) can execute the action, and
- the MCIX runtime can start successfully.

You'll see in the logs the version of the MCIX System Version action you're using as well as some other diagnostic and informational messages.

## Recommended repository layout

For this tutorial, your repository should contain at least the following structure:

```text
mcix-github-actions-demo/
├── .github/
│   └── workflows/
│       └── mcix-system-version.yaml
├── datastage/
├── filesystem/
├── overlays/
└── README.md
```

As the tutorial progresses, you will add an additional workflow file to export, overlay, import, compile, analyse, and test your DataStage assets.

## Summary

Before continuing, confirm that you have:

- DataStage Development and CI projects
- DataStage projects that are not Git integrated
- an API key for DataStage authentication
- test data storage configured where unit tests will run
- a GitHub repository based on the MettleCI template
- GitHub Actions enabled
- a ci GitHub Environment
- environment variables for your DataStage URL, username, and project
- an environment secret containing your API key
- a successful MCIX System Version workflow run

Once these prerequisites are complete, you are ready to build a GitHub Actions workflow using the MCIX custom actions.