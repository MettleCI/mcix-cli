---
title: Generic pipeline 
description: Generic pipeline
# banner_src: ../../assets/img/banner.jpeg
---

<c4d-link-list type="default" slot="complementary">
  <c4d-link-list-heading>Resources</c4d-link-list-heading>
  <c4d-link-list-item
    href="/command-line/command-reference"
    target="cmd-ref"
    cta-type="local"
  >
    MCIX Command Reference
  </c4d-link-list-item>
</c4d-link-list>

---

# Creating a simple CI/CD pipeline

This tutorial shows how to build a basic CI/CD pipeline using MCIX commands to export, transform, import, analyse, and test DataStage assets.

The example pipeline follows this flow:

```text
datastage export
  → overlay apply
  → datastage import
  → asset-analysis test
  → unit-test execute
```

## Scenario

In this example, we assume you have:

* a source watsonx.data integration / CP4D project containing DataStage assets
* a target watsonx.data integration / CP4D project
* an MCIX container image available to your CI/CD platform
* environment-specific overlay files stored in your repository
* asset-analysis and unit-test definitions already available

The pipeline will:

1. Export assets from a source project.
2. Apply environment-specific changes using overlays.
3. Import the modified assets into a target project.
4. Run asset analysis tests.
5. Execute DataStage unit tests.

---

# 1. Repository structure

A simple repository might look like this:

```text
my-datastage-project/
├── overlays/
│   └── dev/
│       └── overlay.yaml
├── tests/
│   ├── asset-analysis/
│   │   └── rules.yaml
│   └── unit-tests/
│       └── unit-test-suite.yaml
└── pipeline/
    └── ci-cd.yml
```

The pipeline will create temporary working folders during execution:

```text
work/
├── exported-assets/
├── overlaid-assets/
├── test-results/
└── reports/
```

---

# 2. Required pipeline variables

Your pipeline should provide the connection details and credentials needed by the MCIX commands.

For example:

```text
CP4D_SOURCE_URL
CP4D_SOURCE_PROJECT
CP4D_SOURCE_USERNAME
CP4D_SOURCE_PASSWORD

CP4D_TARGET_URL
CP4D_TARGET_PROJECT
CP4D_TARGET_USERNAME
CP4D_TARGET_PASSWORD

MCIX_IMAGE
```

Sensitive values such as passwords or API keys should be stored as secrets in your CI/CD platform.

---

# 3. Example pipeline flow

The following example uses a generic shell-based pipeline style. The same structure can be adapted to GitHub Actions, Azure DevOps, Jenkins, Tekton, or another CI/CD system.

```yaml
stages:
  - export
  - overlay
  - import
  - asset-analysis
  - unit-test

variables:
  MCIX_IMAGE: ghcr.io/example/mcix-cli:latest

steps:
  - name: Prepare workspace
    script: |
      mkdir -p work/exported-assets
      mkdir -p work/overlaid-assets
      mkdir -p work/test-results
      mkdir -p work/reports

  - name: Export DataStage assets
    script: |
      docker run --rm \
        -v "$PWD/work/exported-assets:/export" \
        "$MCIX_IMAGE" \
        mcix datastage export \
          --url "$CP4D_SOURCE_URL" \
          --project "$CP4D_SOURCE_PROJECT" \
          --username "$CP4D_SOURCE_USERNAME" \
          --password "$CP4D_SOURCE_PASSWORD" \
          --output-directory /export

  - name: Apply environment overlay
    script: |
      docker run --rm \
        -v "$PWD/work/exported-assets:/input" \
        -v "$PWD/work/overlaid-assets:/output" \
        -v "$PWD/overlays/dev:/overlays" \
        "$MCIX_IMAGE" \
        mcix overlay apply \
          --input-directory /input \
          --overlay-file /overlays/overlay.yaml \
          --output-directory /output

  - name: Import DataStage assets
    script: |
      docker run --rm \
        -v "$PWD/work/overlaid-assets:/import" \
        "$MCIX_IMAGE" \
        mcix datastage import \
          --url "$CP4D_TARGET_URL" \
          --project "$CP4D_TARGET_PROJECT" \
          --username "$CP4D_TARGET_USERNAME" \
          --password "$CP4D_TARGET_PASSWORD" \
          --input-directory /import

  - name: Run asset analysis tests
    script: |
      docker run --rm \
        -v "$PWD/work/overlaid-assets:/assets" \
        -v "$PWD/tests/asset-analysis:/tests" \
        -v "$PWD/work/reports:/reports" \
        "$MCIX_IMAGE" \
        mcix asset-analysis test \
          --input-directory /assets \
          --rules-file /tests/rules.yaml \
          --output-directory /reports \
          --junit-file /reports/asset-analysis-results.xml

  - name: Execute unit tests
    script: |
      docker run --rm \
        -v "$PWD/tests/unit-tests:/tests" \
        -v "$PWD/work/test-results:/results" \
        "$MCIX_IMAGE" \
        mcix unit-test execute \
          --url "$CP4D_TARGET_URL" \
          --project "$CP4D_TARGET_PROJECT" \
          --username "$CP4D_TARGET_USERNAME" \
          --password "$CP4D_TARGET_PASSWORD" \
          --test-suite /tests/unit-test-suite.yaml \
          --junit-file /results/unit-test-results.xml
```

---

# 4. Command-by-command explanation

## Step 1: Export DataStage assets

```bash
mcix datastage export \
  --url "$CP4D_SOURCE_URL" \
  --project "$CP4D_SOURCE_PROJECT" \
  --username "$CP4D_SOURCE_USERNAME" \
  --password "$CP4D_SOURCE_PASSWORD" \
  --output-directory /export
```

This exports the DataStage assets from the source project into a local directory.

In the container example, `/export` is mounted to:

```text
work/exported-assets
```

This ensures the exported files remain available after the container exits.

---

## Step 2: Apply overlays

```bash
mcix overlay apply \
  --input-directory /input \
  --overlay-file /overlays/overlay.yaml \
  --output-directory /output
```

This applies environment-specific configuration changes to the exported assets.

Typical overlay changes might include:

* connection names
* schema names
* database names
* parameter set values
* environment-specific paths
* runtime configuration values

The result is written to:

```text
work/overlaid-assets
```

This directory contains the version of the assets that will be imported into the target environment.

---

## Step 3: Import DataStage assets

```bash
mcix datastage import \
  --url "$CP4D_TARGET_URL" \
  --project "$CP4D_TARGET_PROJECT" \
  --username "$CP4D_TARGET_USERNAME" \
  --password "$CP4D_TARGET_PASSWORD" \
  --input-directory /import
```

This imports the overlaid assets into the target project.

At this point, the target environment has received the transformed version of the assets exported from the source environment.

---

## Step 4: Run asset analysis tests

```bash
mcix asset-analysis test \
  --input-directory /assets \
  --rules-file /tests/rules.yaml \
  --output-directory /reports \
  --junit-file /reports/asset-analysis-results.xml
```

This validates the imported or prepared assets against your asset-analysis rules.

Examples of checks might include:

* naming standards
* prohibited stage types
* required annotations
* parameterisation rules
* connection usage rules
* project compliance rules

The JUnit output can be published by your CI/CD platform so failed checks appear as test failures.

---

## Step 5: Execute unit tests

```bash
mcix unit-test execute \
  --url "$CP4D_TARGET_URL" \
  --project "$CP4D_TARGET_PROJECT" \
  --username "$CP4D_TARGET_USERNAME" \
  --password "$CP4D_TARGET_PASSWORD" \
  --test-suite /tests/unit-test-suite.yaml \
  --junit-file /results/unit-test-results.xml
```

This runs the DataStage unit tests against the target project.

The resulting JUnit file can also be published by the pipeline, giving the team visibility of test failures directly in the CI/CD system.

---

# 5. Example GitHub Actions version

Here is the same flow represented as a GitHub Actions workflow.

```yaml
name: MCIX CI/CD

on:
  workflow_dispatch:
  push:
    branches:
      - main

env:
  MCIX_IMAGE: ghcr.io/example/mcix-cli:latest

jobs:
  deploy-and-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Prepare workspace
        run: |
          mkdir -p work/exported-assets
          mkdir -p work/overlaid-assets
          mkdir -p work/test-results
          mkdir -p work/reports

      - name: Export DataStage assets
        run: |
          docker run --rm \
            -v "$PWD/work/exported-assets:/export" \
            "$MCIX_IMAGE" \
            mcix datastage export \
              --url "${{ secrets.CP4D_SOURCE_URL }}" \
              --project "${{ vars.CP4D_SOURCE_PROJECT }}" \
              --username "${{ secrets.CP4D_SOURCE_USERNAME }}" \
              --password "${{ secrets.CP4D_SOURCE_PASSWORD }}" \
              --output-directory /export

      - name: Apply overlay
        run: |
          docker run --rm \
            -v "$PWD/work/exported-assets:/input" \
            -v "$PWD/work/overlaid-assets:/output" \
            -v "$PWD/overlays/dev:/overlays" \
            "$MCIX_IMAGE" \
            mcix overlay apply \
              --input-directory /input \
              --overlay-file /overlays/overlay.yaml \
              --output-directory /output

      - name: Import DataStage assets
        run: |
          docker run --rm \
            -v "$PWD/work/overlaid-assets:/import" \
            "$MCIX_IMAGE" \
            mcix datastage import \
              --url "${{ secrets.CP4D_TARGET_URL }}" \
              --project "${{ vars.CP4D_TARGET_PROJECT }}" \
              --username "${{ secrets.CP4D_TARGET_USERNAME }}" \
              --password "${{ secrets.CP4D_TARGET_PASSWORD }}" \
              --input-directory /import

      - name: Run asset analysis tests
        run: |
          docker run --rm \
            -v "$PWD/work/overlaid-assets:/assets" \
            -v "$PWD/tests/asset-analysis:/tests" \
            -v "$PWD/work/reports:/reports" \
            "$MCIX_IMAGE" \
            mcix asset-analysis test \
              --input-directory /assets \
              --rules-file /tests/rules.yaml \
              --output-directory /reports \
              --junit-file /reports/asset-analysis-results.xml

      - name: Execute unit tests
        run: |
          docker run --rm \
            -v "$PWD/tests/unit-tests:/tests" \
            -v "$PWD/work/test-results:/results" \
            "$MCIX_IMAGE" \
            mcix unit-test execute \
              --url "${{ secrets.CP4D_TARGET_URL }}" \
              --project "${{ vars.CP4D_TARGET_PROJECT }}" \
              --username "${{ secrets.CP4D_TARGET_USERNAME }}" \
              --password "${{ secrets.CP4D_TARGET_PASSWORD }}" \
              --test-suite /tests/unit-test-suite.yaml \
              --junit-file /results/unit-test-results.xml

      - name: Publish asset analysis results
        uses: actions/upload-artifact@v4
        with:
          name: asset-analysis-results
          path: work/reports/

      - name: Publish unit test results
        uses: actions/upload-artifact@v4
        with:
          name: unit-test-results
          path: work/test-results/
```

---

# 6. Important implementation notes

The exact MCIX command flags may differ depending on your command implementation, so treat the examples above as a pipeline pattern rather than a definitive command reference.

The most important pattern is this:

```bash
-v "$PWD/local-folder:/container-folder"
```

This mounts a local pipeline workspace folder into the MCIX container. Any files written by MCIX inside the mounted container folder remain available to later pipeline steps after the container exits.

For example:

```bash
-v "$PWD/work/exported-assets:/export"
```

allows this command:

```bash
--output-directory /export
```

to write files into:

```text
work/exported-assets
```

on the CI/CD runner.

---

# 7. Final pipeline summary

The complete CI/CD flow is:

```text
Export source assets
  ↓
Apply environment overlay
  ↓
Import assets into target project
  ↓
Run static asset-analysis tests
  ↓
Run runtime unit tests
  ↓
Publish reports and JUnit results
```

This gives you a repeatable deployment pipeline where DataStage assets are exported, transformed, promoted, validated, and tested using MCIX commands in a containerised CI/CD process.
