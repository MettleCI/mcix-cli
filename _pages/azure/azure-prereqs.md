---
title: Azure DevOps<br/>Environment Setup 
description: Prepare your environment for your<br/>MCIX-powered CI/CD Pipeline 
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

Before you start building an Azure DevOps Pipeline there are a number of items you'll need to manually configure a number of items in your Azure DevOps organization and project.  💡 Note that the operations described on this page can be automated, if required, using the [Azure CLI](https://learn.microsoft.com/en-au/cli/azure/?view=azure-cli-latest).  

## Installing the MCIX extension

MCIX is available as an Azure DevOps extension that provides a set of native Azure Pipeline build steps, making it much easier to access MCIX capabilities directly from your pipelines. These build steps are delivered through a Visual Studio Marketplace extension. To use them in your organization’s build pipelines, you must first install the extension into your Azure DevOps organization.

To install the extension ...

1. Navigate to your Azure DevOps organization and select **Organization settings** (gear icon). <br/>⚠️ *Ensure sure you navigate to the Organization settings, not the repository settings.*
1. Under the **Overview** section, select **Extensions**.
1. Click the **Browse marketplace** button to access the Visualstudio Marketplace. 
1. Search for 'mcix', select it, and on the resulting page click **Get it free**. 
1. Select your organization from the dropdown menu. <br/>⚠️ *If you do not see your organization in the dropdown, ensure you are signed into the Visual Studio Marketplace with the same identity used in your Azure DevOps tenant.*
1. For installations on Azure DevOps Service (SaaS) 
- click **Install**.
1. For installations on Azure DevOps Server (on-premises)
- Click **Download** to save the extension as a `.vsix` file
- Navigate to the **Manage Extensions** page and upload the `.vsix` file directly.

### Verfying your extension installation

To verify the extension has installed ...

1. Navigate to your Azure DevOps organization and select **Organization settings** (gear icon).
1. Under the **Overview** section, select **Extensions**.
1. Navigate to the **Installed** tab and click the entry for the mcix extension.
1. On the resulting page you'll see the version and publication date of the extension.

### Removing the extension

To disable or remove the extension ...

1. Navigate to your Azure DevOps organization and select **Organization settings** (gear icon).
1. Under the **Overview** section, select **Extensions**.
1. Navigate to the **Installed** tab and click the entry for the mcix extension.
- The extension can be disabled by clicking the dot menu (⠇) button at the top of the page and selecting **Disable**.
- The extension can be uninstalled from your organization by clicking the **Uninstall** button at the top of the page.


## Creating a Service Connection

The MCIX extension for Azure DevOps provides a set of native Azure Pipeline build steps that simplify access to MCIX functionality. These build steps know how to invoke the MCIX command line, but they also need to know where to find the runtime container image that provides the MCIX command. 

To do this you'll create a Service Connection to the Container Registry hosting the MCIX container image, then provide each MCIX build step with a reference that Service Connection.

To create a Service Connection ...

1. Navigate to your Project's **Project Settings** → **Service connections** and select **New service connection**.  
1. Choose 'Docker Registry' and click **Next**.
1. Select your registry type (i.e. *Azure Container Registry*, *Docker Hub*, or *Others*). 
  - The default public container registry is the IBM Container Registry (`icr.io`) for which you should select *Others*. 
1. For an Azure Container Registry ...
  - Select **Managed Service Identity** or **Service Principal** as the authentication type. Refer to the Azure DevOps documentation for details on how to configure the relevant options for each of these selections. 
  - Provide the Subscription ID, Subscription Name, and Login Server. 
1. For *DockerHub* or *Others*: 
  - Enter the registry URL, Username, and Password (or Access Key).
1. Give the Service Connection a name (e.g. `acr-mcix-container`)
1. Check **Grant access permission to all pipelines** to make the connection available to all builds. 
1. Click **Verify and Save**.


## Defining your Environments

An Azure DevOps **Environment** is a logical deployment target such as `Dev`, `Test`, `QA`, `Staging`, or `Production`. Pipelines can deploy to these environments and Azure DevOps will keep deployment history, approvals, and checks against them.

1. Navigate to your Azure DevOps project (Azure DevOps → Your organisation → Your project)
1. In the left-hand navigation, select **Pipelines** → **Environments**
1. Create a new environment by clicking **New environment**.
1. Enter the environment name and description. See the [CI Concepts](/getting-started/ci-concepts) for a list of environments used in the example pipelines accompanying MCIX.
1. Choose the resource type 'None' to give you a simple environment used only for deployment tracking and approvals.
1. Create the environment by clicking **Create**.

### Add optional approvals and checks

For controlled environments such as `Production` it can be useful to restrict who can perform a deployment to this environment, and when that deployment can be performed.  You do this on the Environemnt's Approvals and Checks tab.

Approvals and Checks are defined on your Environment and control the execution order of pipeline stages.  An Environment can have multiple different type of approvals and checks configured but for our purposes we're going to define a pre-check approval which will need to be authorised by a used with the relevant authority before a pipeline stage which uses this environment will be executed. If tgis pre-check approval is rejected or times out, the stage is not executed.

1. Open **Pipelines** → **Environments** → **\<environment\>** then navigate to the **Approvals and checks** tab.
1. Select **\+** (Add check).
1. Check the **Approvals** checkbox and click **Next**.
1. Select the user(s) who may approve a deployment and, optionally, specify some brief instructions for them.
1. Under **Advanced** you may optionally select the **Allow approvers to approve their own runs** checkbox.
1. Under **Control options** you may optionally specify the timeout period for an approval request.

This allows you to require manual approval before a pipeline deploys to that environment. 

<details markdown="1">
  <summary>Referencing an Environment from within a YAML pipeline</summary>
To deploy to an environment, use a `deployment` job rather than a normal `job`. e.g.
```yaml
{% raw %}stages:
- stage: DeployProd
  displayName: Deploy to Prod
  jobs:
    - deployment: MCIX_Deploy_Prod
      displayName: Deploy to Prod
      environment: PROD
      strategy:
        runOnce:
          deploy:
            steps:
            - checkout: self
            - task: mcixDataStageDeploy@1
              displayName: "Deploy repository to ${{ variables.EnvID }}"
              inputs:
                containerRegistry: 'acr-docker-mcix'
                imageName: "mettleci.azurecr.io/mettleci/mcix"
                imageTag: "1"

                # Overlay parameters
                assets: "datastage"
                overlays: |
                  'overlays/common'
                  'overlays/prod'
                properties: "varfiles/var.PROD"

                # DataStage connection details
                url: $(HostName)
                user: $(UserName)
                apiKey: "$(APIKey)"
                project: ${{ variables.Datastage_Project }}
{% endraw %}```

The key line is the `enviroment` element which must match the environment name you created in your **Environments** page:

```yaml
environment: PROD
```

In this example, `Production` should have an approval check configured so that the stage pauses until someone approves the deployment.
</details>

## Variables and Secrets

An Azure DevOps variable group is a reusable collection of named values that can be shared across multiple pipelines, helping you centralise common configuration such as image names, service connection names, environment URLs, or deployment settings.

Variable groups can also contain secret variables, where sensitive values such as passwords, API keys, tokens, or credentials are encrypted and hidden from pipeline logs while still being available securely to pipeline tasks.

To create a **Variable Group** in Azure DevOps:

1. Navigate to your Azure DevOps project (Azure DevOps → Your organisation → Your project)
1. In the left-hand navigation, select **Pipelines** → **Library**
1. Select **+ Variable group**
1. Give the variable group a name (e.g. `mcix-vars`)
1. Optionally add a description (e.g. `Shared MCIX pipeline configuration`)
1. Under **Variables**, click **+ Add**.
1. Add your variables, for example:

   | Name                                 | Value                               |
   | ------------------------------------ | ----------------------------------- |
   | HostName   | value | description |
   | UserName   | value | description |
   | APIKey   | value | description |
   | DatastageProject: ${{ variables.Datastage_Project }}"
   | EnvironmentID: ${{ variables.EnvID }}"

1. For sensitive values, click the **lock** icon (🔓) beside the value to mark it as secret.
1. Click **Save**.<br/>
<br/>

<details markdown="1">
  <summary>Referencing a Variable from within a YAML pipeline</summary>
At the top of your Azure Pipeline YAML file, reference the group like this:
```yaml
{% raw %}variables:
- group: mcix-settings
{% endraw %}```

Then use the variables in your pipeline steps:

```yaml
{% raw %}steps:
- script: |
    echo "Using MCIX container image: $(containerImage)"
  displayName: Show container image
{% endraw %}```

For example, if you want to use the same container image across multiple custom tasks:

```yaml
{% raw %}variables:
- group: mcix-settings

steps:
- task: MettleCI.mcix.import@1
  inputs:
    containerImage: $(containerImage)
    containerRegistryServiceConnection: $(containerRegistryServiceConnection)

- task: MettleCI.mcix.compile@1
  inputs:
    containerImage: $(containerImage)
    containerRegistryServiceConnection: $(containerRegistryServiceConnection)
{% endraw %}```

The YAML syntax for referencing a variable group is:

```yaml
{% raw %}variables:
- group: my-variable-group
{% endraw %}```

where `group` must be the first property in that entry.
</details>

## Other Settings

- You **do not** need to define any *Agent Pools* as MCIX runs using a container privisioned by Azure DevOps itself.
- You can enable *Parallel jobs* (**Project settings** → **Parallel jobs**) for your Microsoft-hosted jobs as there are steps within a typical DataStage NextGen CI/CD pipeline which can exhibit improved performance when run in parallel.
