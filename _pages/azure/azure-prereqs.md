---
title: Azure DevOps Pipeline Prerequisites 
description: Set up the building blocks of your MCIX-powered Azure DevOps Pipeline 
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

The MCIX extension for Azure DevOps provides a set of native Azure Pipeline build steps which greatly simplifies access to MCIX functionality.  The build steps installed by the MCIX extension know how to use the MCIX command line, but need to know where they can find the runtime container image within which the MCIX command is available. This is done by creating a Service Connection to a Container Registry where the MCIX container is hosted and providing each MCIX build step with a reference to this Service Connection.

To create a Service Connection ...

1. Navigate to **Project Settings** → **Service connections** and select **Create service connection**.  
1. Choose 'Docker Registry' and select your registry type (e.g., Azure Container Registry or Others). 
1. The default container registry is IBM Container Registry
1. For Azure Container Registry
  - Select **Managed Service Identity** or **Service Principal** as the authentication type.
  - Provide the Subscription ID, Subscription Name, and Login Server. 
1. For Others (UsernamePassword): 
  - Enter the registry URL, Username, and Password (or Access Key).  Check Grant access permission to all pipelines to make the connection available to all builds. 

