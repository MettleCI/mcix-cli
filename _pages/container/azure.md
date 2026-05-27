---
title: Azure DevOps Task Extension 
description: Native MCIX tasks for Azure DevOps
# banner_src: ../../assets/img/banner.jpeg
---

<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/card-group.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block-mixed.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/link-list.min.js"></script>

<c4d-link-list type="default" slot="complementary">
  <c4d-link-list-heading>Resources</c4d-link-list-heading>
  <c4d-link-list-item
    href="https://marketplace.visualstudio.com/items?itemName=MettleCI.mcix"
    target="mcix-azure"
    cta-type="external"
  >
    MCIX for Azure DevOps on Visual Studio Marketplace
  </c4d-link-list-item>
</c4d-link-list>

## Introduction

Like GitHub users, Azure DevOps users (both Server and SaaS) can also take advantage of native pipeline tasks. The **MCIX Azure DevOps Task Extension**, available in the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=MettleCI.mcix){:target="_blank" rel="noopener"} provides a number of native tasks for use in Azure DevOps CI/CD pipelines - again, underpinned by the MCIX container image which is nosted automtically by your Azure DevOps runner. For example:

## Example

### Command Line Pipeline Task

```yaml
- stage: Export
  pool:
    vmImage: "ubuntu-latest"
  jobs:
    - job: MCIX_Export
      steps:
        - bash: |
            ./some-location/mcix datastage export \
              -api-key ${API_KEY} \
              -url ${CPD_URL} \
              -user ${CPD_USER} \
              -project ${CPD_PROJECT} \
              -export-path ${EXPORT_PATH}
          displayName: "Run export command"
```

### Azure DevOps Native Task

```yaml
- stage: Export
  pool:
    vmImage: "ubuntu-latest"
  jobs:
    - job: MCIX_Export
      steps:
        - task: mcixDatastageExport@1
          inputs:
            containerRegistry: "my-docker-service-connection"
            imageName: "mettleci.azurecr.io/mettleci/mcix"
            api-key: ${API_KEY}
            url: ${CPD_URL}
            user: ${CPD_USER}
            project: ${CPD_PROJECT}
            assets: ${EXPORT_PATH}
          displayName: "Export DataStage Assets"
```

## Architecture

```mermaid
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
  %% Azure DevOps environment
  %% =========================
  subgraph ADO["Azure DevOps Environment"]
      subgraph ADOREPO["Git Repository"]
        ADOPIPEDEF["CI/CD Pipeline<br/>Definition"]
      end
      subgraph ADORUN["Azure DevOps Runner"]
        ADOPIPERUN["Azure DevOps<br/>Pipeline"]
        subgraph ADOT["Azure DevOps Tasks"]
          ADOCONT["MCIX container instance"]
        end
      end
  end
  class ADOT tooling
  class ADOCONT runtime

  %% =========================
  %% Distribution from registry
  %% =========================
  IMG -. Pull .-> ADOCONT

  %% ADO Tooling references
  ADOPIPEDEF --> ADOPIPERUN
  ADOPIPERUN <--> ADOT
  ADOT <--> ADOCONT

  %% Action/Task links to CPD
  ADOCONT <--> CPD

```

## Setup

There are a number of mandatory and recommendedf processes you'll need to perform to be able to use the Aziure Devops extensions