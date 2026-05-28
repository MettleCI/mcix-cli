<div align="center">

<img src="assets/img/mci_logo.svg" alt="Git Switch" width="96" height="96" />

# MCIX Command Line Interface for DataStage NextGen

A fast, native client that provides all your CI/CD requirements for IBM DataStage NextGen.

[![macOS](https://img.shields.io/badge/macOS-Apple_Silicon-green?logo=apple&logoColor=white)](#install)
[![Linux](https://img.shields.io/badge/Linux-x86__64-orange?logo=linux&logoColor=black)](#install)
[![Windows](https://img.shields.io/badge/Windows-x86__64-blue?logo=windows&logoColor=white)](#install)
[![Apache2.0](https://img.shields.io/badge/License-Apache2.0-yellow.svg)](LICENSE)

</div>

---

# MCIX CLI

**MettleCI automation for IBM DataStage NextGen and watsonx.data integration.**

> [!CAUTION]
> This repository is provided as a **technology preview** which may change, break, or disappear at any point and without warning.

MettleCI is IBM's official solution for providing DevOps automation for IBM DataStage teams, helping organisations improve quality, repeatability, and confidence across the software delivery lifecycle.  

MCIX is a command-line toolkit for automating common DataStage NextGen delivery tasks such as analysing assets, applying overlays, importing project content, compiling assets, and producing CI/CD-friendly evidence such as JUnit XML reports.  It is designed to be used from a developer workstation, inside a build agent, or as part of a containerised delivery workflow in any CI/CD platform capable of running command-line tools or Docker containers.

---

## Why MCIX?

Modern DataStage delivery requires more than manual export/import operations. Teams need repeatable, auditable, automated workflows that can validate changes, promote assets between environments, and provide clear pass/fail feedback to CI/CD platforms.

MCIX is the tools enat enables you to ...

* Automate DataStage NextGen asset export, import, and compilation
* Apply environment-specific overlays before deployment
* Run automated checks as part of a build or release pipeline
* Produce JUnit XML output for CI/CD test reporting
* Package repeatable delivery workflows into scripts, pipelines, or containers
* Standardise how teams interact with IBM Cloud Pak for Data and watsonx.data integration environments

---

## Typical use cases

MCIX can be used to support workflows such as:

* Exporting DataStage assets from a development project
* Applying overlays to make exported assets suitable for another environment
* Importing assets into a target project
* Compiling imported assets
* Running asset analysis or compliance checks
* Publishing JUnit XML reports to a CI/CD platform
* Building reusable CI/CD pipelines using GitHub Actions, Azure DevOps, Jenkins, or other CI/CD tools 

---

## Repository contents

This repository provides:

* Public documentation for the MCIX CLI
* Release assets containing platform-specific MCIX binaries for Windows, Linux, and macOS.
* Examples for using MCIX from the command line

---

## Installation

Download the appropriate archive from the latest GitHub release:

* `mcix-linux-x86.zip`
* `mcix-macos-arm64.zip`
* `mcix-windows-x86.zip`

Unzip the archive and place the `mcix` executable somewhere on your `PATH`.

For example, on Linux or macOS:

```bash
unzip mcix-linux-x86.zip -d mcix
sudo install mcix/mcix /usr/local/bin/mcix
mcix --version
```

On Windows, extract the archive and add the extracted directory to your `PATH`.

---

## Quick start

Display the available namespaces and commands:

```bash
mcix help
```

Display help for a namespace:

```bash
mcix help datastage
```

Display help for a specific command:

```bash
mcix help datastage import
```

Further examples of how to use MCIX commands can be found in the [MCIX documentation](https://cli.mettleci.io/).

---

## CI/CD integration

MCIX is intended to integrate easily with common delivery platforms:

* **GitHub Actions** — run MCIX directly on a runner or inside a container step
* **Azure DevOps** — run MCIX from shell scripts or through custom Azure DevOps tasks
* **Jenkins** — call MCIX from pipeline stages, shared libraries, or Docker agents
* **Other platforms** — run MCIX anywhere command-line tools or Docker containers are supported

A typical pipeline will:

1. Check out the repository containing DataStage assets
2. Download or pull the MCIX runtime
3. Apply overlays for the target environment
4. Import assets into the target project
5. Compile the imported assets
6. Publish any generated JUnit XML files as test results
7. Archive deployment logs and other evidence

---

## Authentication

Most commands that connect to IBM Cloud Pak for Data or watsonx.data integration require connection details such as:

* CPD or Software Hub URL
* User name
* API key
* Project name or identifier

We recommend using environment variables, or even better your CI/CD platform's secret-management feature, rather than placing credentials directly in scripts.

Example:

```bash
export CPD_URL="https://cpd.example.com"
export CPD_USER="my-user"
export CPD_APIKEY="..."
```

Then pass those values to MCIX:

```bash
mcix datastage import \
  --url "$CPD_URL" \
  --user "$CPD_USER" \
  --api-key "$CPD_APIKEY" \
  --project "My DataStage Project" \
  --assets "./dist/datastage"
```

---

## Documentation

The MCIX documentation site is available at [https://cli.mettleci.io/](https://cli.mettleci.io/).

Use the documentation for detailed command reference material, examples, and release-specific guidance.

---

## Releases

MCIX binaries are published through GitHub Releases.

Each release may include platform-specific archives such as:

* Linux x86
* macOS Apple Silicon
* Windows x86

Use the latest release unless you need to pin a specific version for reproducible builds.

---

## Project status

MCIX is actively evolving to support automated delivery workflows for IBM DataStage NextGen and watsonx.data integration.

Command names, options, and release packaging may change between versions. Pin the MCIX version used by production pipelines and test upgrades before rolling them out broadly.

---

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.
