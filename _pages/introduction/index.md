---
title: MCIX Introduction
description: Welcome to the MettleCI Command Line Interface for DataStage Nextgen
type: introduction
order: 1
# banner_src: ../../assets/img/banner.jpeg
---

# Introduction

The MCIX command provides a set of capabilities underpinning the creation of automated CI/CD pipelines for any modern build tool.

| **Migration** | - Providing facilities to migrate MettleCI test assets from DataStage v11.x to DataStage NextGen. |
| **Deployment operations** | - Importing and exporting assets to/from DataStage NextGen environments<br/> - Compiling assets in DataStage NextGen<br/>- Automatically adapting properties of assets to suit their target environments |
| **Testing** | - Invoking static asset analysis (the equivalent of [lint](<https://en.wikipedia.org/wiki/Lint_(software)>){:target="_blank" rel="noopener"} for DataStage NextGen assets)<br/>- Fabricating synthetic test data based on custom test data specifications<br/>- Dynamic unit testing (executing your DataStage NextGen flows using a restricted set of test data) |

These capabilities are supplied by the MCIX command which itself is available in various forms:

- A native **terminal command** (Linux, macOS, or Windows) 
- A **container image**
- A set of native CI/CD **build task** (Azure DevOps, GitHub Actions, and Jenkins)

```mermaid
  %%{init:{'flowchart':{'nodeSpacing': 50, 'rankSpacing': 50}}}%%
  flowchart TD

  %% =========================
  %% Styles
  %% =========================
  classDef registry fill:#333333,stroke:#3b82f6,stroke-width:2px,color:#111;
  classDef image fill:#eefbf3,stroke:#22c55e,stroke-width:2px,color:#111;
  classDef runtime fill:#fff7e6,stroke:#f59e0b,stroke-width:2px,color:#111;
  classDef tooling fill:#f5ecff,stroke:#8b5cf6,stroke-width:2px,color:#111;
  classDef plugin fill:#ffffff,stroke:#6b7280,stroke-width:1px,color:#111;
  classDef command fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#111;
  classDef highlight fill:#f4f4f4,stroke:#0f62fe,stroke-width:4px,color:#161616;

  %% CPD
  subgraph CPD["IBM Software Hub"]
    WATSONX["DataStage NextGen"]
  end


  %% Command
  subgraph HOST["Host"]
    subgraph SHELL["Operating System"]
        MCIXCMD["mcix command"]:::highlight
    end
  end
  class MCIXCMD highlight;
  MCIXCMD <--> WATSONX

  %% Docker
  subgraph DOCKERHOST["Host"]
    subgraph DOCKER["Docker"]
      subgraph MCIX_CNT["Container"]
          MCIXCMD_CNT["mcix command"]
      end
    end
  end
  class MCIX_CNT highlight;
  MCIXCMD_CNT <--> WATSONX

  %% Task
  subgraph CICD["Azure / GitHub / Jenkins"]
    subgraph CICD_TASK["Build Tasks"]
      subgraph MCIX_CNT_CICD["Container"]
          MCIXCMD_CNT_CICD["mcix command"]
      end
    end
  end
  class CICD_TASK highlight;
  MCIXCMD_CNT_CICD <--> WATSONX
```


## Terminal Command

The MCIX CLI terminal command provides the ability to interactively explore MCIX's capabilities without requiring additional software or infrastructure.  It is described in more detail [here](../command-line/command-shell){:target="_blank" rel="noopener"}.

The command is available for **Unix (x86)**, **Windows (x86)**, and **macOS (ARM64)**, all downloadable from [here](https://github.com/mettleci/mcix-cli/releases/latest){:target="_blank" rel="noopener"}.


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

The MCIX container provides all the capablities of the MCIX command line with the deployment flexibility of a container.  This form of MCIX provides the fundamental building block of your automated CI/CD processes for watsonx.data integration. It is described in more detail [here](../container/container){:target="_blank" rel="noopener"} and is hosted [here](https://github.com/MettleCI/mcix/pkgs/container/mcix){:target="_blank" rel="noopener"}. 

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

Users of the most popular CI/CD orchestration tools can make use of native pipeline tasks which enable them to reference MCIX operators directory from within their pipeline YAM files. MCIX tasks, introduced [here](../container/native-tasks), are available for ...

- [Azure DevOps](../azure/azure)
- [GitHub](../github/github)
- [Jenkins](../jenkins/jenkins)

```mermaid
  flowchart TD

  %% =========================
  %% Styles
  %% =========================
  %% classDef registry fill:#333333,stroke:#3b82f6,stroke-width:2px,color:#111;
  %% classDef image fill:#eefbf3,stroke:#22c55e,stroke-width:2px,color:#111;
  %% classDef runtime fill:#fff7e6,stroke:#f59e0b,stroke-width:2px,color:#111;
  %% classDef tooling fill:#f5ecff,stroke:#8b5cf6,stroke-width:2px,color:#111;
  %% classDef plugin fill:#ffffff,stroke:#6b7280,stroke-width:1px,color:#111;
  %% classDef command fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#111;

  %% =========================
  %% GitHub environment
  %% =========================
  subgraph CICD["CI/CD Environment"]
      subgraph CICDREPO["Git Repository"]
        CICDPIPE["CI/CD Pipeline<br/>Definition"]
      end
      subgraph GHRUN["CI/CD Task Runner"]
        CICDACT["CI/CD<br/>Pipeline"]
        subgraph CICDA["CI/CD Tasks"]
          CICDCONT["MCIX container<br/>instance"]
        end
      end
  end
  class CICDA tooling
  class CICDCONT runtime

  %% CICD Tooling references
  CICDPIPE --> CICDACT
  CICDACT <--> CICDA
  CICDA <--> CICDCONT

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
  %% class REG registry

  subgraph CPD["IBM Software Hub"]
    DATASTAGE["DataStage NextGen"]
  end

  %% =========================
  %% Distribution from registry
  %% =========================
  IMG -. Pull .-> CICDCONT

  %% Action/Task links to CPD
  CICDCONT <--> CPD
```
