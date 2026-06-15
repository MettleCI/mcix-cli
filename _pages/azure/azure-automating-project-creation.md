---
title: Automating your Azure DevOps<br/>Project Setup 
description: Prepare your environment for your<br/>MCIX-powered CI/CD Pipeline 
# banner_src: ../../assets/img/banner.jpeg
---

<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block-mixed.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/link-list.min.js"></script>

<c4d-link-list type="default" slot="complementary">
  <c4d-link-list-heading>Resources</c4d-link-list-heading>
  <c4d-link-list-item
    href="https://learn.microsoft.com/en-us/azure/devops/cli/?view=azure-devops&utm_source=chatgpt.com"
    target="mcix-docs"
    cta-type="local"
  >
    Quickstart: Get started with Azure DevOps CLI
  </c4d-link-list-item>
  <c4d-link-list-item
    href="https://learn.microsoft.com/en-us/rest/api/azure/devops/distributedtask/environments?view=azure-devops-rest-7.1"
    target="azure-automation"
    cta-type="external"
  >
    Environments - REST API
  </c4d-link-list-item>
  <c4d-link-list-item
    href="https://learn.microsoft.com/en-us/rest/api/azure/devops/approvalsandchecks/check-configurations/get?view=azure-devops-rest-7.1"
    target="mcix-github"
    cta-type="external"
  >
    Check Configurations - Get - REST API
  </c4d-link-list-item>
</c4d-link-list>


# Introduction

The MettleCI Azure DevOps pipeline examples require several Azure DevOps resources, including:

* Azure DevOps projects
* Repositories
* Agent pools and self-hosted agents
* Deployment environments
* Environment approvals and checks
* Variable groups
* Pipeline definitions

These resources can be created manually in Azure DevOps, but doing so repeatedly is time-consuming and error-prone. This guide explains how to automate much of that setup using the Azure CLI and Azure DevOps REST APIs.

## Recommended Azure DevOps structure

When configuring Azure DevOps for MettleCI pipelines, there are two common approaches.

### Option 1: One Azure DevOps project containing multiple repositories

In this model, a single Azure DevOps project contains repositories for multiple MettleCI/DataStage projects.

This approach requires you to:

* Create one repository for each MettleCI/DataStage project
* Create CI, QA, Test, Production, and other deployment environments within the same Azure DevOps project
* Configure permissions carefully so that each project team can access only the repositories, pipelines, and environments they require

### Option 2: One Azure DevOps project per DataStage project

In this model, each DataStage project is represented by a separate Azure DevOps project.

Each Azure DevOps project contains:

* A default repository for the DataStage assets
* The pipeline definitions for that DataStage project
* The environments required by that project
* The variable groups required to connect to the relevant DataStage and MettleCI platforms

This approach usually requires less configuration and is easier to reason about, so it is the approach used in this guide.

## Prerequisites

Before running the automation examples, ensure you have the following:

* The Azure CLI installed
* The Azure DevOps CLI extension installed
* Access to the target Azure DevOps organisation
* A Personal Access Token, or PAT, with sufficient permissions to create and update:

  * Azure DevOps projects
  * Repositories
  * Agent pools (Not requried when using the Azure DevOps MCIX tasks)
  * Pipelines
  * Variable groups
  * Environments
  * Environment approvals and checks

The order in which you privision these should be...

```
Create Azure DevOps project
        ↓
Create repositories
        ↓
Create variable groups
        ↓
Create environments
        ↓
Create environment approvals and checks
        ↓
Create MCIX container registry service connection
        ↓
Create or import pipeline definitions
```

## Example automation assets

MettleCI provides an example repository containing scripts and examples that demonstrate how to create the Azure DevOps assets required for a working MettleCI-enabled pipeline.

The examples cover the following resource types.

| Azure DevOps asset     | Description                                                                                                                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Projects               | Azure DevOps projects provide the top-level container for repositories, boards, pipelines, environments, and related configuration.                                                       |
| Agent pools and agents | Agent pools contain the agents that execute pipeline jobs. MettleCI pipelines typically use self-hosted agents with the required DataStage, MettleCI, and runtime dependencies installed. |
| Environments           | Environments represent deployment targets such as CI, Test, QA, Pre-Production, or Production. They can also be protected using approvals and checks.                                     |
| Repositories           | A typical MettleCI setup uses one repository for DataStage assets and another for compliance rules.                                                                                       |
| Variable groups        | Variable groups store reusable pipeline configuration such as DataStage hostnames, credentials, project names, and MettleCI settings. Secret values should be marked as secret variables. |
| Pipelines              | Pipeline definitions describe the CI, deployment, hotfix, and upgrade workflows used to test and promote DataStage assets.                                                                |

## Agent pools and self-hosted agents

The MCIX Azure DevOps tasks mean that you are not required to:

- provision a self-hosted Azure DevOps agent
- install MCIX on an agent machine
- configure custom agent capabilities
- create a dedicated MCIX agent pool

Azure Pipelines always runs jobs on an agent, but when using the MCIX Azure DevOps tasks a Microsoft-hosted Azure Pipelines agent is sufficient. The MCIX Azure DevOps tasks provide access to the MCIX runtime by using the MCIX container image configured by your Project's Service Connection. 

A self-hosted agent may still be required in some environments, but usually for network or security reasons rather than because of MCIX itself. Where network access permits, a Microsoft-hosted Azure Pipelines agent is sufficient. 

## Repositories

A typical MettleCI Azure DevOps project requires two repositories:

| Repository                  | Purpose                                                          |
| --------------------------- | ---------------------------------------------------------------- |
| DataStage asset repository  | Stores exported DataStage assets and related project files.      |
| Compliance rules repository | Stores the compliance rules used by MettleCI compliance testing. |

The supplied automation examples include commands to create these repositories and import the sample content.

## Variable groups

Variable groups store shared pipeline configuration.

You will normally need one variable group for each DataStage platform that your pipelines interact with. For example:

* Development
* CI
* QA
* Pre-Production
* Production

Each variable group should contain the values required by the corresponding pipeline stage, such as hostnames, project names, usernames, and passwords.

Passwords and other sensitive values should be stored as secret variables. If your organisation requires secrets to be managed in Azure Key Vault, modify the supplied examples to reference Key Vault-backed variables instead.

<cds-inline-notification
  kind="warning"
  title="Caution"
  subtitle="We have observed cases where Azure DevOps creates a secret variable but does 
  not correctly assign its value. If this occurs, update the secret value manually in 
  the Azure DevOps administration console."
  low-contrast
  hide-close-button="true"
  id="overlay-notification">
</cds-inline-notification>

To add a secret variable to an existing variable group:

```bash
az pipelines variable-group variable create \
  --org <ORGANISATION_URL> \
  --project <PROJECT_NAME> \
  --group-id <GROUP_ID> \
  --name <VARIABLE_NAME> \
  --secret true \
  --value <VARIABLE_VALUE>
```

## Example pipelines

The example repository includes the following pipeline definitions.

| Pipeline            | Purpose                                                                                                                                                                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `devops-ci.yml`     | A standard CI pipeline triggered by commits to the DataStage asset repository. It demonstrates compliance testing, unit testing, and deployment to downstream environments.                                                                                   |
| `hotfix-ci.yml`     | Performs compliance and unit testing against a hotfix-specific branch.                                                                                                                                                                                        |
| `hotfix-deploy.yml` | Deploys a hotfix branch directly to the production DataStage environment.                                                                                                                                                                                     |

## Creating an approvers group

Approvals should normally be applied only to official deployment environments, such as:

* Test
* QA
* Pre-Production
* Production

They should not normally be applied to internal CI environments, because requiring approval for CI deployments would slow down the development feedback loop.

If approvals are required, create an appropriate Azure DevOps group from the Azure DevOps administration console.

Then retrieve the group details using the Azure DevOps CLI:

```bash
az devops security group list \
  --org <ORGANISATION_URL> \
  --scope organization \
  --query "graphGroups[?displayName=='<GROUP_NAME>'] | [0]"
```

The response will include values similar to the following:

```json
{
  "originId": "<GROUP_ORIGIN_ID>",
  "principalName": "<GROUP_PRINCIPAL_NAME>"
}
```

Record these values. They are used later when creating an approval check for an environment.

## Creating an environment

Azure DevOps environments can be created using the Azure DevOps REST API. Microsoft documents the environment creation operation under the Distributed Task Environments API. ([Microsoft Learn][1])

First, encode your PAT for use with basic authentication.

The leading colon before the PAT is required:

```bash
echo -n ':<PERSONAL_ACCESS_TOKEN>' | base64
```

Then create the environment:

```bash
curl -X POST \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Basic <ENCODED_COLON_THEN_PAT>' \
  'https://dev.azure.com/<ORGANISATION_NAME>/<PROJECT_NAME>/_apis/distributedtask/environments?api-version=7.1' \
  -d '{
    "name": "<ENVIRONMENT_NAME>",
    "description": "<ENVIRONMENT_DESCRIPTION>"
  }'
```

Record the `id` value returned in the response. This value is used as `<ENVIRONMENT_ID>` when configuring approvals and checks.

## Adding an approval check to an environment

To protect an environment with an approval, create an approval check configuration for that environment.

The Azure DevOps Checks Configuration API uses API version `7.1-preview.1`. ([Microsoft Learn][4])

```bash
curl -X POST \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Basic <ENCODED_COLON_THEN_PAT>' \
  'https://dev.azure.com/<ORGANISATION_NAME>/<PROJECT_NAME>/_apis/pipelines/checks/configurations?api-version=7.1-preview.1' \
  -d '{
    "type": {
      "id": "8C6F20A7-A545-4486-9777-F762FAFE0D4D",
      "name": "Approval"
    },
    "settings": {
      "approvers": [
        {
          "displayName": "<GROUP_PRINCIPAL_NAME>",
          "id": "<GROUP_ORIGIN_ID>"
        }
      ],
      "executionOrder": 1,
      "blockedApprovers": [],
      "minRequiredApprovers": 1,
      "requesterCannotBeApprover": false
    },
    "resource": {
      "type": "environment",
      "id": "<ENVIRONMENT_ID>",
      "name": "<ENVIRONMENT_NAME>"
    }
  }'
```

The `type.id` value shown above identifies the Azure DevOps approval check type. It is not specific to your project, pipeline, or environment, and should be used exactly as shown.
