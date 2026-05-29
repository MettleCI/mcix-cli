---
title: Native CI/CD Tasks
description: Native MCIX tasks for popular CI/CD orchestration tools
# banner_src: ../../assets/img/banner.jpeg
---

<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/card-group.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block-mixed.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/link-list.min.js"></script>

<c4d-link-list type="default" slot="complementary">
  <c4d-link-list-heading>Resources</c4d-link-list-heading>
  <c4d-link-list-item
    href="https://github.com/marketplace?query=mcix"
    target="github-marketplace"
    cta-type="external"
  >
    MCIX on GitHub Marketplace
  </c4d-link-list-item>
  <c4d-link-list-item
    href="https://marketplace.visualstudio.com/items?itemName=MettleCI.mcix"
    target="mcix-azure"
    cta-type="external"
  >
    MCIX for Azure DevOps on Visual Studio Marketplace
  </c4d-link-list-item>
  <c4d-link-list-item
    href="https://marketplace.visualstudio.com/items?itemName=MettleCI.mcix"
    target="mcix-jenkins"
    cta-type="external"
  >
    MCIX Jenkins Custom Tasks on GitHub
  </c4d-link-list-item>
</c4d-link-list>

As well being available as a [terminal command](../command-shell/command-shell) and a [Docker container image](../container/container), the individual commands provided by the MCIX command shell are also available as native tasks for the most popular CI/CD orchestration tools.

The XXXXX native tasks provide richer deeper integration and richer feedback than terminal commands while also requiring no additional infrastructure, oer the use of remote GitHub runners. For example:

MXIX features enabled by the Azure DevOps integration
<!-- - Commit to Azure DevOps-managed Git repositories -->
<!-- - Retrieve Compliance Rules from a Azure DevOps-managed Git repository -->
<!-- - Perform a live lookup of Azure DevOps work items for users to select from when they are performing a Git commit. -->
- Execute sophisticated CI/CD Azure DevOps Pipelines for Information Server using the MCIX Command Line Interface
- Provide Unit Test and Integration Test results as Azure DevOps-compatible JUnit test reports -->
<!-- - Provide Compliance, Unit Test, and Integration Test results as Azure DevOps-compatible JUnit test reports -->

Custom tasks are currentl avaialbe for the following platforms:
- GitHub Custom Actions
- Azure DevOps Task Extension
- Jenkins Custom Tasks


## Composite Tasks

There are some instances where combinations of MCIX commands aere frequently executed in combination with one another.  
A good example of this is the process of deploying DataStage assets to a target environment:

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

  subgraph HOST["host"]
    HOSTDIR["Host dir"]
  end
  subgraph DEPLOY["Deploy"]
    DEPLOY_START
    MCIX_OVERLAY["mcix datastage export"]
    MCIX_OVERLAY_OUT["overlay out"]
    MCIX_IMPORT["mcix datastage import"]
    MCIX_IMPORT_OUT["import out"]
    MCIX_COMPILE["mcix datastage compile"]
    MCIX_COMPILE_OUT["compileout"]
    DEPLOY_END
  end
    DEPLOY_START --> MCIX_OVERLAY
    MCIX_OVERLAY --> MCIX_OVERLAY_OUT
    MCIX_OVERLAY --> MCIX_IMPORT
    MCIX_IMPORT --> MCIX_IMPORT_OUT
    MCIX_IMPORT --> MCIX_COMPILE
    MCIX_COMPILE --> MCIX_COMPILE_OUT
    MCIX_COMPILE --> DEPLOY_END

  HOST -. Call .-> DEPLOY_START
  DEPLOY_END -. Return .-> HOST

```
