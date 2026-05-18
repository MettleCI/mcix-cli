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
    MCIX Azure DevOps Tasks
  </c4d-link-list-item>
</c4d-link-list>

As well being available as a terminal command and a Docker container image, the individual commands provided by the MCIX command shell are also available as native tasks for the most popular CI/CD orchestration tools.

## GitHub Custom Actions

When using GitHub as your CI/CD orchestration tool you can take advantage of the **MCIX GitHub Actions** available in the [GitHub Marketplace](https://github.com/marketplace?query=mcix){:target="_blank" rel="noopener"}. These actions provide GitHub-native tasks which are underpinned by the MCIX container image. The GitHub native tasks provide richer deeper integration and richer feedback than terminal commands while also requiring no additional infrastructure, oer the use of remote GitHub runners. For example:

**Command Line**

```yaml
jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
      - name: DataStage export using the mcix datastage export command within a bash shell
        run: bash \
          ${GITHUB_WORKSPACE}/some-location/mcix datastage export \
          -api-key ${API_KEY} \
          -url ${CPD_URL} \
          -user ${CPD_USER} \
          -project ${CPD_PROJECT} \
          -export-path ${EXPORT_PATH}
```

**GitHub Actions Native Action**

```yaml
jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
      - name: DataStage export using the mcix datastage export GitHub action
        uses: mettleci/mcix/datastage/export@latest
        with:
          api-key: ${API_KEY}
          url: ${CPD_URL}
          user: ${CPD_USER}
          project: ${CPD_PROJECT}
          assets: ${EXPORT_PATH}
```

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
  %% GitHub environment
  %% =========================
  subgraph GH["GitHub Environment"]
      subgraph GHREPO["Git Repository"]
        GHPIPE["CI/CD Pipeline<br/>Definition"]
      end
      subgraph GHRUN["GitHub Actions Runner"]
        GHACT["GitHub Actions<br/>Pipeline"]
        subgraph GHA["GitHub Actions"]
          GHCONT["MCIX container instance"]
        end
      end
  end
  class GHA tooling
  class GHCONT runtime

  %% GH Tooling references
  GHPIPE --> GHACT
  GHACT <--> GHA
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

## Azure DevOps Task Extension

Like GitHub users, Azure DevOps users can also take advantage of native pipeline tasks. The **MCIX Azure DevOps Task Extension**, available in the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=MettleCI.mcix){:target="_blank" rel="noopener"} provides a number of native tasks for use in Azure DevOps CI/CD pipelines - again, underpinned by the MCIX container image. For example:

**Command Line**

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

**Azure DevOps Native Task**

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

## Jenkins Custom Tasks

DataStage users who use Jenkins for their CI/CD pipelines can make use of the MCIX Jenkins Library to provide their pipelines with native MCIX steps.

**Command line**
```yaml
stage("Deploy - CI") {
    agent { label 'mcix-capable' }
    steps {
        withCredentials([
          string(credentialsId: ${CPD_APIKEY_CRED}, variable: 'CP4DAPIKEY')
        ]) {
            sh label: 'Export DataStage Assets',
                script: """#!/bin/bash
                    ./some-location/mcix datastage export \
                        -api-key ${CP4DAPIKEY} \
                        -url ${CPD_URL} \
                        -user ${CPD_USER} \
                        -project ${CPD_PROJECT} \
                        -export-path ${EXPORT_PATH}
                """
        }
    }
}
```

**Jenkins Custom Task**

This first example uses a Docker-capable agent.

```yaml
@Library('mcix-jenkins-lib') _
pipeline {
    stages {
        stage("Export") {
  	        agent { label 'docker-capable' }
            steps {
                mcixDatastageExport(
                    registryUrl: "${MCIX_CONTAINER_REG_URL}",
                    registryCredentialsId: "${MCIX_CONTAINER_REG_CRED}",
                    image: "${MCIX_CONTAINER_IMAGE}",
                    url: "${CPD_URL}",
                    user: "${CPD_USER}",
                    apiKeyCredentialsId: "${CPD_APIKEY_CRED}",
                    project: "${CPD_PROJECT}",
                    assets: "${EXPORT_PATH}",
                )
           }
        }
    }
}
```

This second example uses the MCIX container itself as the execution environment.

```yaml
@Library('mcix-jenkins-lib') _
pipeline {
    stages {
        stage("Export") {
            agent {
                docker {
                    registryUrl 'https://ghcr.io'
                    registryCredentialsId 'GHCR'
                    image 'ghcr.io/mettleci/mcix:latest'
                    args "-u root --entrypoint=''"
                }
            }
            steps {
                mcixDatastageExport(
                    url: "${CPD_URL}",
                    user: "${CPD_USER}",
                    apiKeyCredentialsId: "${CPD_APIKEY_CRED}",
                    project: "${CPD_PROJECT}",
                    assets: "${EXPORT_PATH}"
                )
            }
        }
    }
}
```