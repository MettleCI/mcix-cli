---
title: Jenkins Pipeline Tutorial Prerequisites
description: Establishing the conditions for a pipeline using MCIX Jenkins tasks
---

Before you begin this tutorial you’ll need to prepare your DataStage projects, Git repository, Jenkins environment configuration, and the credentials required to connect Jenkins tasks to your DataStage service.

<cds-inline-notification
  kind="warning"
  title="Important"
  low-contrast
  hide-close-button="true"
  id="overlay-notification">
  <div>
  Ideally, this tutorial would not require you to install the MCIX CLI on your local host as there would be a suitable direct interface between the DataStage user interface and your Git platform. However, due to the requirement for the <a href="/notes/git-interface">interim Git Interface</a>, you should start this tutorial by following the <a href="/command-line/tutorial-prerequisites#install-the-mcix-command-line">Install the MCIX command line</a> section of the Command Line tutorial.
  </div>
</cds-inline-notification>

---

## Configure your DataStage projects

Ensure you have a DataStage NextGen project for each of the environments you use during the tutorial:

1. Your source `Development` environment, and
2. Each environment to which you wish to deploy.

For the purposes of this tutorial we’ll use a single CI target environment.

| Environment | Project name |
| :---        | :--- |
| Development | `mcix-demo` |
| CI          | `mcix-demo_ci` |

Ensure your DataStage NextGen projects are not configured as Git integrated projects.

- Do not select **Git Integrated** when creating the project.
- Do not select **Enable Git integration** in the settings of the created project.

In this tutorial your Git repository is the source of truth for your DataStage assets. DataStage projects represent environment-specific deployments of that source.

## Generate an API key

If you don’t yet have one, generate an API key for the user account that GitHub Actions will use to connect to DataStage.

The type of key you need to generate depends on whether you are using DataStage NextGen on a self-hosted platform or IBM Cloud-hosted DataStage-as-a-Service.

#### Self-hosted

Create an API key using IBM’s guidance for your platform. Depending on your IBM Software Hub / Cloud Pak configuration, this may be either:

- a platform API key, or
- an instance API key.

#### SaaS

For IBM Cloud-hosted DataStage-as-a-Service, create an **IBM Cloud API key**, not a Cloud Pak API key.

Note that the value of an IBM Cloud API key is only available for download/copy at creation time. The copy icon shown next to an existing key copies the key ID, not the secret key value.

## Configure DataStage test data storage

As part of this tutorial you may execute unit tests against one or more DataStage flows.  To support this, configure test data storage in the DataStage project where tests will be executed. For this tutorial, that will normally be your CI project.  

If you want to use the sample project provided with this tutorial then ensure that your test data storage connection is called `TestDataConnection`.

## Prepare Git repositories

Before running a Jenkins-based MCIX pipeline, you need two Git repositories:
 - a global library repository containing the MCIX custom steps
 - a repository containing the pipeline Jenkinsfiles, your DataStage assets, overlays, and any supporting files.

Use simple, purpose-based repository names, such as:

```text
mcix-global-lib
mcix-jenkins-pipeline-demo
```

Avoid naming the template repository after a specific environment, such as myproject-prod or myproject-test. The repository should represent the single source of truth for the DataStage initiative, not one particular deployment target.

Recommended settings for your repositories:

| Setting           | Value                        |
| :---------------- | :-------------------------   |
| Repository name   | `mcix-shared-lib`<br>`mcix-jenkins-pipeline-demo` |
| Visibility        | Private                      |
| Default branch    | `main`                       |
| `.gitignore`      | Yes                          |
| README            | Yes                          |


You may be presented with additional options when creating the repositories, depending on your choice of Git repositiory hosting platform.
For this introductory tutorial, keep the repository simple so you can focus on the pipeline mechanics.

## Clone the MettleCI template repositories

MettleCI template repositories are provided for both the global library and template repository, for convenience and as a recommended starting point.

#### MCIX Global Library Repository

Clone the global library repository to your local host:

```shell
git clone https://github.com/MettleCI/datastage-nextgen-jenkins-libs
```

Rename the local directory to match your new GitHub repository:

```shell
mv datastage-nextgen-repo-template mcix-global-lib
```
The contents of this repository do not need to be modified, but contain the MCIX custom commands that the template pipeline uses.
Now point the local clone to your new Git repository:

```shell
git remote set-url origin <YOUR_NEW_GLOBAL_LIBRARY_REPOSITORY_URL>
```
For example:

```shell
git remote set-url origin git@my-git-host.com:my-org/mcix-global-lib.git
```
Push the template contents to your new repository:

```shell
git push -u origin main
```


#### MCIX Template Repository

You are not required to follow the template repository’s structure. You can organise your repository in 
whatever way best suits your project, including where you store DataStage assets, scripts, configuration 
files, documentation, and other non-DataStage artefacts.

The template repository does, however, demonstrate a practical best-practice layout that is easy to understand, 
easy to deploy, and suitable for most delivery pipelines.

Clone the template repository to your local host:

```shell
git clone https://github.com/MettleCI/datastage-nextgen-repo-template
```

Rename the local directory to match your new GitHub repository:

```shell
mv datastage-nextgen-repo-template mcix-jenkins-pipeline-demo
cd mcix-jenkins-pipeline-demo
```

Inspect the repository contents:

```shell
ls -al
```
You should see a structure similar to this:

```shell
mcix-jenkins-pipeline-demo/
├── .git
├── .gitattributes
├── .gitignore
├── datastage/
├── filesystem/
├── overlays/
└── README.md
```

Now point the local clone to your new GitHub repository:

```shell
git remote set-url origin <YOUR_NEW_PIPELINE_REPOSITORY_URL>
```
For example:

```shell
git remote set-url origin git@github.com:my-org/mcix-jenkins-pipeline-demo.git
```
Push the template contents to your new repository:

```shell
git push -u origin main
```
You can now open your Git repository in a browser and confirm that the template files are visible.

## Add Plugins to the Jenkins Server

In your Jenkins server, navigate to: <br/>
**Jenkins** → **Manage Jenkins** → **Plugins** → **Available Plugins**

For this tutorial, you will need to install some additional plugins:
 - Docker Pipeline (this will also install a number of pre-requisite Docker plugins)
 - JUnit
 - Pipeline: Basic Steps

## Jenkins Agent Requirements

MCIX template functions run inside a Docker container running a custom image based on Debian Linux 
that contains the MCIX cli.
Therefore, the Jenkins agent should be running a flavour of Linux and have a working Docker engine.

For instructions on how to install the Docker angine and configure it to work with Jwnkins, lease refer to
 - [Install Docker Engine](https://docs.docker.com/engine/install/)
 - Also follow the post-installation step to add the jenkins user to the docker group.

It must also have network access to:
- your Git repository,
- the MCIX hared library repository,
- the MCIX container image registry, and
- your DataStage service URL.

## Create Jenkins Credentials

Create a Jenkins credential to store the API Key of the Cloud Pak DataStage user
In your Jenkins server, navigate to: <br/>
**Jenkins** → **Manage Jenkins** → **Credentials**

At the end of the page, the is a section **Stores scoped to Jenkins**
Click on the link for **Global**

In the top right-hand corner, click **Add Credentials**

| Setting             | Value             | Description                                       |
| :------------------ | :---------------- | :------------------------------------------------ |
| `Kind`              | `Secret text`     | Select from the dropdown                          |
| `Secret`            | CPD User API Key  | API Key for the User used to connect to DataStage |
| `ID`                | `CP4D_APIKey`     | Referred to in the agent environment variable     |

You will also need to add the Git Credentials that allow you to connect to the newly-created global library repository and pipeline repository. 


## Configure Jenkins Agent

Configure the Jenkins agent: <br/>
**Jenkins** → **Manage Jenkins** → **Nodes**

Select the node that contains the Docker engine
On the left-hand side, select **Configure**

Then add the following environment variables:

| Variable            | Example value             | Description                                   |
| :------------------ | :------------------------ | :-------------------------------------------- |
| `CP4D_URL`          | `https://cpd.example.com` | Base URL of your DataStage service            |
| `CP4D_USER`         | `my-user@example.com`     | Username used to connect to DataStage         |
| `CP4DAPIKEY`        | `CP4D_APIKey`             | Name of the credential containing the API Key |


## Configure Jenkins Server to Recognise the MCIX Global Library Repository

Configure the Jenkins agent: <br/>
**Jenkins** → **Manage Jenkins** → **System**
Scroll down the page to **Global Trusted Pipeline Libraries**, and at the bottom of that section, click **Add**

| Setting                                          | Value                                      | Description                                   |
| :----------------------------------------------- | :----------------------------------------- | :-------------------------------------------- |
| `Name`                                           | `mcix-global-lib`                          | The alias referred to in pipelines            |
| `Default version`                                | `main`                                     | Repository branch                             |
| `Load implicitly`                                | false                                      |                                               |
| `Include @Library changes in job recent changes` | false                                      |                                               |
| `Retrieval method`                               | `Modern SCM`                               |                                               |
| `Source Code Management`                         | `Git`                                      |                                               |
| `Project Repository`                             | `<YOUR_NEW_GLOBAL_LIBRARY_REPOSITORY_URL>` | The URL of the Global Library Repository      |
| `Credentials`                                    | Select the repository access credential    |                                               |
| `Library path`                                   | `./`                                       |                                               |

## Create the Jenkins Pipeline

To create the pipeline: <br/>
On the **Jenkins** homepage, select **New Item**. 
Enter a name for the pipeline, for example: 

```
mcix-ci
```

Under **Select an item type**, click on **Pipeline**
Click on **Ok**

On the next Page, select the following settings:

| Section          | Setting                                          | Value                                      | Description                                   |
| :--------------- | :----------------------------------------------- | :----------------------------------------- | :-------------------------------------------- |
| `General`        | `Do not allow concurrent builds`                 | true                                       | Only run one of this pipeline at a time       |
| `Triggers`       | `Poll SCM`                                       | true                                       | Poll the repository                           |
|                  | `Schedule`                                       | `* * * * *`                                | Poll once per minute                          |
| `Pipeline`       | `Definition`                                     | `Pipeline script from SCM`                 |                                               |
|                  | `SCM`                                            | `Git`                                      |                                               |
|                  | `Repository URL`                                 | `<YOUR_NEW_PIPELINE_REPOSITORY_URL>`       | The URL of the Global Library Repository      |
|                  | `Credentials`                                    | Select the repository access credential    |                                               |
|                  | `Branch Specifier (blank for 'any')`             | `*/main`                                   |                                               |
|                  | `Script Path`                                    | `pipelines/mcix-ci-jenkinsfile`            |                                               |


## Create the pipelines directory

Create a directory for pipeline files:

```bash
mkdir -p pipelines
```
## Add a simple MCIX verification workflow

Before building the full pipeline, create a simple workflow that verifies your repository can execute an MCIX action.

Create this file which will create a simple workflow using the [MCIX system version](/github/action-reference#system-version) action:

```
pipelines/mcix-ci-jenkinsfile
```

Add the following content:

```
@Library('mcix-jenkins-lib') _

pipeline {
    // Specify an agent that runs a Docker server where the MCIX cons=tainer image can be hosted
    agent none

    // Sets up the environment for the build
    environment {
        IIS_BASE_PROJECT_NAME = 'mcix-demo'
    }

    stages {

        // Dumps diagnostic values to the execution log (optional)
        stage("Diagnostics") {
            agent {
                docker {
                    registryUrl 'https://docker.io'
                    image 'docker.io/mettleci/mcix:latest'
                    args "-u root --entrypoint=''"
                    alwaysPull true
                }
            }
            environment {
                ENVID = "ci"
                DATASTAGE_PROJECT = "${env.IIS_BASE_PROJECT_NAME}_${env.ENVID}"
            }

            steps {
                // Call the MCIX system version command to verify the MCIX command in the image is available
                mcixSystemVersion()
            }
        }
    }
}
```

We'll run through the role of this file and meaning of each line in the [tutorial steps](tutorial-steps). For now, commit and push the workflow:

```shell
git add pipelines/mcix-ci-jenkinsfile
git commit -m "Add MCIX system version workflow"
git push
```


## Recommended repository layout

For this tutorial, your repository should contain at least the following structure:

```text
mcix-jenkins-pipwline-demo/
├── pipelines/
│   └── mcix-ci-jenkinsfile
├── datastage/
├── filesystem/
├── overlays/
└── README.md
```

As the tutorial progresses, you will add an additional workflow file to export, overlay, import, compile, analyse, and test your DataStage assets.

## Summary

Before continuing, confirm that you have:

- DataStage Development and CI projects
- DataStage projects that are not Git integrated
- an API key for DataStage authentication
- test data storage configured where unit tests will run
- a Git repository based on the MCIX Global Library repository
- a Git repository based on the MCIX template
- Jenkins Credentials
    - CPD API Key
    - access credentials to the Git repositories
- Jenkins agent capable of running Linux-based Docker containers
    - With environment variables configured
- Global Library repository added to Jenkind system configuration
- Jenkins Pipeline for the MCIX template Jenkinsfile
- a successful MCIX System Version pipeline run

Once these prerequisites are complete, you are ready to build a Jenkins Pipeline using the MCIX Jenkins tasks.