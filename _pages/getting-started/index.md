---
title: MCIX Introduction
description: Welcome to the MettleCI Command Line Interface for DataStage Nextgen
type: introduction
order: 1
# banner_src: ../../assets/img/banner.jpeg
---

The MCIX command provides a set of capabilities underpinning the creation of automated CI/CD pipelines for any modern build tool.

| **Deployment operations** | - Importing and exporting assets to/from CPD environments<br/> - Compiling assets in CPD<br/>- Automatically adapting properties of asset to suit their target environments |
| **Testing** | - Invoking static asset analysis (the equivalent of [lint](<https://en.wikipedia.org/wiki/Lint_(software)>){:target="_blank" rel="noopener"} for DataStage NextGen assets)<br/>- Fabricating synthetic test data based on custom test data specifications<br/>- Dynamic asset analysis (executing your DataStage NextGenn flows using a restricted sets of test data) |

These capabilities are supplied by the MCIX command which itself is available in various forms:

- Terminal Command
- Container Image
- GitHub Custom Actions
- Azure DevOps Task Extensions
- Jenkins Things

## Terminal Command

The MCIX CLI terminal command is available for **Linux (x86)**, **Windows (x86)**, and **macOS (ARM64)**, all downloadable from [here](https://github.com/mettleci/mcix-cli/releases/latest){:target="_blank" rel="noopener"}.

While not necessarily being the most _useful_ mode of operation, the MCIX terminal command provides the ability to interactively explore MCIX's capabilities without requiring additional software or infrastructure.

```mermaid
  %%{init:{'flowchart':{'nodeSpacing': 50, 'rankSpacing': 50}}}%%
  flowchart LR

  %% =========================
  %% Styles
  %% =========================
  classDef registry fill:#333333,stroke:#3b82f6,stroke-width:2px,color:#111;
  classDef image fill:#eefbf3,stroke:#22c55e,stroke-width:2px,color:#111;
  classDef runtime fill:#fff7e6,stroke:#f59e0b,stroke-width:2px,color:#111;
  classDef tooling fill:#f5ecff,stroke:#8b5cf6,stroke-width:2px,color:#111;
  classDef plugin fill:#ffffff,stroke:#6b7280,stroke-width:1px,color:#111;
  classDef command fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#111;

  %% =========================
  %% Shell
  %% =========================
  %% Image internals
  subgraph SHELL["Operating System"]
      subgraph MCIX["mcix command"]
        PLUGINS@{ shape: procs, label: "MCIX Plugins"}
      end
      %% GOV["Container Governance Artefacts"]
  end
  class SHELL image
  class MCIX command
  class PLUGINS plugin

  subgraph CPD["IBM Software Hub"]
    DATASTAGE["DataStage NextGen"]
  end

  MCIX <--> CPD
```

## Container Image

MCIX is also available as a Docker container image hosted [here](https://github.com/MettleCI/mcix/pkgs/container/mcix){:target="_blank" rel="noopener"}. This mode of delivery provides the fundamental building block of your automated CI/CD processes for DataStage NextGen.

```mermaid
  flowchart LR

  %% =========================
  %% Styles
  %% =========================
  classDef registry fill:#333333,stroke:#3b82f6,stroke-width:2px,color:#111;
  classDef image fill:#eefbf3,stroke:#22c55e,stroke-width:2px,color:#111;
  classDef runtime fill:#fff7e6,stroke:#f59e0b,stroke-width:2px,color:#111;
  classDef tooling fill:#f5ecff,stroke:#8b5cf6,stroke-width:2px,color:#111;
  classDef plugin fill:#ffffff,stroke:#6b7280,stroke-width:1px,color:#111;
  classDef command fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#111;

  %% =========================
  %% GitHub environment
  %% =========================
  subgraph GH["Runtime Environment"]
      GHCONT["MCIX container instance"]
      GHA["CI/CD Orchestrator"]
  end
  class GHA tooling
  class GHCONT runtime

  %% GH Tooling references
  GHA <--> GHCONT

  %% =========================
  %% Registry
  %% =========================
  subgraph REG["Container Registry"]
      %% Image internals
      subgraph IMG["MCIX Container Image"]
      subgraph MCIX["mcix command"]
        PLUGINS@{ shape: procs, label: "MCIX Plugins"}
      end
      end
      class MCIX command
      class PLUGINS plugin
      class IMG image
  end
  %% class IMG image
  %% class REG registry

  subgraph CPD["IBM Software Hub"]
    DATASTAGE["DataStage NextGen"]
  end

  %% =========================
  %% Distribution from registry
  %% =========================
  IMG -. Pull .-> GHCONT

  %% Action/Task links to CPD
  GHCONT <--> CPD

```

## Native CI/CD Tasks

The individual commands provided by the MCIX command shell are also available as [native tasks](native-tasks) for the most popular CI/CD orchestration tools:

- GitHub
- Azure DevOps
- Jenkins
