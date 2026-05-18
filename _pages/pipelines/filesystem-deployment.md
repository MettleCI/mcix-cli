---
classification: confidential #Remove this line if it's not IBM Confidential.
status: draft #Status can be draft, reviewed or published. 
owner: Add the main page authors
tags:
  - Pipelines
---
# Filesystem deployment

## Introduction

MettleCI will handle the management and deployment of DataStage Assets, Project Environment Variables and Parameter Sets.  However, most ETL processes consistent of more than just DataStage jobs and will usually require additional file system assets in order to function correctly.  Just like DataStage jobs and sequences, these file system assets should be checked into version control and automatically deployed and tested as part of your MettleCI deployment pipeline.

Examples of file system assets which typically form part of an ETL solution:

* Shell Scripts
* DataStage schema files
* SQL Scripts
* Directory Structures
* Reference Data Files
* Configuration Files

Unlike DataStage assets, the process of deploying file system assets is highly dependent on the design of each ETL solution.  Unfortunately, the heterogeneous nature of file system assets makes it all but impossible for MettleCI to include a one-size-fits-all deployment process.  Instead, MettleCI provides a simple, extensible mechanism to quickly build your own file system asset deployment process which is executed by MettleCI.

This guide will first explain how file system asset deployments are performed by MettleCI and then discuss some best practices intended to ensure your automated deployments are both repeatable and easy to maintain.

## Deployment Process

Regardless of whether a deployment is being performed as part of Continuous Integration or Release Deployment, MettleCI will complete the following steps:

1. Create target DataStage project (if it doesn’t exist)
1. Apply environment specific changes to DSParams and deploy to target DataStage project
1. Apply environment specific changes to Parameter Set Value files and deploy to target DataStage project
1. Execute file system deployment
1. Import DataStage assets
1. Compile DataStage assets

File system deployments are executed after the DataStage project has been created but before the DataStage Import and Compile steps are triggered.  This means that at the time of file system deployment, the target DataStage project directory will already exist while still allowing the deployment of any file system assets which might need to be in place before DataStage compilation commences (eg. Header files used by Build Ops or Basic Routines).

Everything required for file system deployment lives within the filesystem directory inside the Git repository for the DataStage project being deployed.  At a minimum, the filesystem components of a DataStage project Git directory structure should contain:

```
┆
├── datastage
│   └── DSParams
└── filesystem
    └── deploy.sh
```

During file system deployment, MettleCI will (recursively) transfer the entire contents of the filesystem directory to a temporary directory on the DataStage engine that hosts the target DataStage project.  MettleCI will then source dsenv and execute the deploy.sh script on the DataStage engine with the following arguments:

```shell
deploy.sh -p <datastage project> -e <environment>
```

The idea is that all file system assets are checked into the filesystem directory in Git and the deploy.sh script will be called during deployment to move the files into the correct location on the DataStage engine.  When deploy.sh is executed, the current working directory is set to be the previously-mentioned temporary directory. This allows any files checked into the filesystem directory to be referenced and accessed within deploy.sh through the use of relative paths.

The parameters <datastage project> and <environment> refer to the name of the target DataStage project and the logical environment name (eg. CI, TEST, PROD, etc) respectively. Note that <environment> should ideally align with the related var.* override file and the Environment postfix.

### Example

As a simple example of how filesystem deployments should work, consider a DataStage project that depends on the following directory structure in order to function:

```
┆
└── data
    └── example_prod
        ├── scripts
        │   ├── wait_for_file.sh
        │   └── transfer_file.sh
        ├──reference
        │   ├── valid_countries.csv
        │   └── system_accounts.csv
        ├── input
        ├── output
        └── transient
```

The following table describes the purpose of each of directory:

| Directory | Purpose |
|-----------|---------|
| scripts   | Contains all shell scripts required by this project. |
| reference | Contains static reference data used for lookups during job execution. |
| input | Folder where external system will place input files processed by this project. |
| output | Folder where data produced by this project is placed for consumption by external systems. |
| transient | Folder containing transient files created during execution of this project but not required after the current ETL batch has completed. |

To automatically deploy this file system with MettleCI, we first need to check in all the scripts and reference files into Git somewhere under the filesystem directory. The *.sh and *.csv file could be checked directly into the root of the filesystem directory structure but maintenance is easier if the Git directory structure closely matches the deployed file system.  We also need to check-in deploy.sh, resulting in a directory structure in Git which looks like this:

```
┆
├── datastage
└── filesystem
    ├── scripts
    │   ├── wait_for_file.sh
    │   └── transfer_file.sh
    ├── reference
    │   ├── valid_countries.csv
    │   └── system_accounts.csv
    └── deploy.sh
```

???+ info "This example excludes the `input`, `output` and `transient` directories in Git"

    This is because
    1. Git only version-controls files, not directories since, strictly speaking, a directory is a property of a file; and
    1. The deploy.sh script creates these folders at deploy time, as the following instructions explain.

Finally, the content of the `deploy.sh` shell script would be:

```bash
#!/bin/sh
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Validate input arguments
# 

USAGE="${0} syntax:
-p <project name> -e <environment>"

while getopts e:w: OPT
do
    case $OPT in
    p)  PROJECT_NAME=${OPTARG} ;;
    e)  ENV_NAME=${OPTARG} ;;
    ?)  echo ${USAGE}
        exit -1 ;; 
    esac
done

# Environment required
if [[ "${ENV_NAME}x" = "x" ]]; then
    echo "ERROR: Parameter <environment> is required.\n${USAGE}";
    exit -1;
fi

# Project required
if [[ "${PROJECT_NAME}x" = "x" ]]; then
    echo "ERROR: Parameter <project name> is required.\n${USAGE}";
    exit -1;
fi

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Deploy filesystem
#

# directory structures
mkdir -p /data/${PROJECT_NAME}/scripts
mkdir -p /data/${PROJECT_NAME}/reference
mkdir -p /data/${PROJECT_NAME}/input
mkdir -p /data/${PROJECT_NAME}/output
mkdir -p /data/${PROJECT_NAME}/transient

# scripts
rm -rf /data/${PROJECT_NAME}/scripts/*
cp -r ./scripts/* /data/${PROJECT_NAME}/scripts/

# reference data
rm -rf /data/${PROJECT_NAME}/reference/*
cp -r ./reference/* /data/${PROJECT_NAME}/reference/

# clear transient files when running Continuous Integration
if [[ "$ENV_NAME" = "CI" ]]; then
    rm -rf /data/${PROJECT_NAME}/transient
fi
```

There are a few important things to note about this script:

 - The first half of `deploy.sh` contains boilerplate validation code.  This can be re-used across all your `deploy.sh` scripts, or externalized into a shared utility script.
 - All required directories are created, if they don’t already exist, using `mkdir -p`
 - Rather than copy each Project script or reference file individually, `deploy.sh` deletes the existing content of the `scripts` and `reference` directories and replaces it with the files being deployed. This keeps `deploy.sh` easy to maintain and understand and also means that the file system is automatically cleaned up when files are removed from Git.
 - The `input` and `output` directories are created but not populated as these directories are expected to be populated by external systems.
 - The `${ENV_NAME}` variable can be used to perform deployment steps specific to a given environment.  In this example we clear the transient directory for Continuous Integration (CI), an explanation of why you may want to do this is covered in the Best Practices section.

### Best Practices

#### Keep Git file system directory structure as close to the deployed directory structure as possible

When the file system directory in Git does not match that of the DataStage engine, developers will need to inspect the deploy.sh script to figure out how one directory structure maps to the other.   Keeping the Git and DataStage engine directory structure closely aligned keeps things simple and reduces debugging and maintenance effort.

#### Clear and deploy directories, not individual files

Rather than writing deploy.sh to move each each and every file individually, deploy entire directories in one go by first performing an rm -rf and followed by cp -r (see scripts and reference data in the previous example).  This approach not only reduces how often the deploy.sh script needs to be changed but it also ensures that old files are automatically removed as part of the deployment process.  

For example, imagine your DataStage project contained a script called legacy_script.sh that was originally checked into the Git directory /filesystem/scripts and which was removed in a later revision of the project.  If the deploy.sh script just had a long list of shell scripts to copy (including our legacy_script.sh), the legacy_script.sh file would never be removed when we deploy new versions.  Worse still, any ETL job or sequence still referring to that script would still pass in testing as legacy_script.sh may still exist on the file system.  By clearing the scripts directory on the DataStage engine, then copying all scripts from /filesystem/scripts in Git, legacy_script.sh would be removed automatically as part of deployment and any ETL jobs or sequences still referring to it would (correctly) fail during testing.

#### Don’t put files from multiple projects in one directory structure

When a single directory structure contains files from multiple projects, it is impossible to clear files in a directory during one project deployment without negatively affecting the other projects.  Always ensure that a file can be identified as being “owned” by a particular project based on the directory structure or file naming convention.

For example, lets say we have two DataStage projects with the following filesystem structure in Git:


```
┆
├── project_1
│   ├── datastage
│   └── filesystem
│       ├── scripts
│       │   ├── copy_files.sh
│       │   └── rename_file.sh
│       └── deploy.sh
└── project_2
    ├── datastage
    └── filesystem
        ├── scripts
        │   ├── wait_for_file.sh
        │   └── transfer_file.sh
        └── deploy.sh
```

If both of these projects deployed their scripts directory to a common directory on the DataStage engine called `/data/scripts/`, it would contain `copy_files.sh`, `rename_files.sh`, `wait_for_file.sh` and `transfer_file.sh`.  Therefore it would not be possible for the `project_1` deployment process to clear all the scripts without also removing scripts from `project_2`.  Additionally, if both projects happened to have a script of the same name, the version in the scripts directory will change depending on which project was most recently deployed.

By ensuring the DataStage engine directory structure is separated by project (e.g., `/data/scripts/<project>/`, `/<project>/scripts/`, `/data/<project>/scripts/`, etc.), it's clear which project 'owns' the scripts.  Otherwise, an approach which is less conventional but just as effective is to copy scripts to a common directory but to add a project identifier prefix or suffix to each file's name.  In this case, the `/data/scripts/` directory could contain `project1_copy_file.sh`, `project1_rename_files.sh`, `project2_wait_for_file.sh` and `project2_transfer_file.sh`.  The `deploy.sh` script could then clear the scripts directory by running `rm -rf /data/scripts/<project>_*`.

#### Clear transient files that are created and used in a single ETL batch

Most ETL processes are composed of multiple DataStage jobs which are executed in sequence and communicate by writing to and reading from files.  When these files are transient and are only expected to live for the life of a single batch, it is good practice to remove them as part of the file system deployment process.   Doing so ensures that problems introduced when renaming files or removing upstream jobs are quickly identified during test execution.

For example, consider the following simple ETL process consisting of three jobs and the resulting design when `Job B` is removed

![file dependencies](./images/dependencies-before.png "file dependencies")

If transient files are not removed as part of the deployment process, then `Job C` will continue to run (invalidly) during testing because `File B` would still exist on the file system from previous executions.  By deleting all transient files (`File A` and `File B`), running the ETL process in testing would (validly) fail when executing Job C and the problem could be quickly detected and corrected.  The same issue can occur if a developer renames files written or read by jobs without ensuring all other jobs are correctly updated to reflect the change.

#### Be careful when deleting Dataset files

As documented by IBM, the structure of a DataStage Dataset means that they cannot simply be deleted by removing just the descriptor file (often named with a *.ds extension).  One solution to clearing file system directories that may contain datasets is to use ...

```
find -name “*.ds” | xargs -l orchadmin delete
```

... to clean up any Datasets before performing `rm -rf` on a directory.  This is effective but can be quite slow.

If all datasets are transient, an alternative approach is to ensure each project writes Dataset segments to its own directory using resource disks in the `$APT_CONFIG_FILE`.  Using this approach you can remove all `*.ds` files for the project using normal rm commands and the Dataset segment files can be removed by clearing the project specific resource disks.

For example, consider the `$APT_CONFIG_FILE` for a DataStage project called example_prod:

```
{
        node "node1"
        {
                fastname "ds-engn.datamigrators.io"
                pools ""
                resource disk "/data/datasets/example_prod" {pools ""}
                resource scratchdisk "/data/scratch" {pools ""}
        }
        node "node2"
        {
                fastname "ds-engn.datamigrators.io"
                pools ""
                resource disk "/data/datasets/example_prod" {pools ""}
                resource scratchdisk "/data/scratch" {pools ""}
        }
}
```

Because the configured resource disk contains only Dataset segment files used by our `example_prod` project and we know DataStage datasets are transient and are not required after ETL Batch execution is complete, we can simply perform `rm /data/datasets/example_prod` to clear all DataStage segment files for this project.  The remaining `*.ds` descriptor files can then be treated like regular files. 
