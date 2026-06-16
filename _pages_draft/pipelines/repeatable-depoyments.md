---
status: reviewed #Status can be draft, reviewed or published. 
owner: John Mckeever
tags:
  - Pipelines
---
# Repeatable DataStage Project Deployments

## Introduction

CI/CD Pipelines will deploy a version of software across multiple environments while subjecting it to harder and harder tests in order to be confident that the software works as intended.  As a result, a core component of any CI/CD Pipeline is to be able to repeatably deploy a given version of software to multiple environments without introducing any differences.  Differences between software deployed across different testing environments can trigger random test failures, or worse, software that worked in testing can fail once deployed to production.

MettleCI provides a set of composable deployment tools for performing repeatable and efficient DataStage Project deployments.

## Deployment of job designs

### Incremental Deployment

A simple but naïve approach to deploying ISX files containing assets with design information would be as follows:

1. Tear down any existing DataStage project in the target environment
1. Create a new DataStage project in the target environment
1. Import all ISX files
1. Compile all jobs in the DataStage project.

This approach is repeatable as the content of the resulting DataStage project will always match the software version represented by the source ISX files.  However, performance of this approach is extremely poor and will not allow the resulting CI/CD Pipelines to provide fast feedback to developers.  As an example, a DataStage project containing about 500 jobs will typically take over 1.5hrs to perform both the import and compile steps of this deployment approach.

The implementation used by the MettleCI [deploy command](../../mettleci-cli/datastage-namespace/#datastage-deploy) is logically equivalent to the naïve approach but uses an incremental algorithm to deploy changes in a fast and scalable manner:

1. Source ISX files and the existing DataStage project are analyzed for differences
1. Differences are converted to operations which transform the existing DataStage project to match the source ISX files
1. An impact analysis of changes caused by step 2 is performed and all affected jobs are compiled (eg. if a shared container changed, then all jobs using it will be compiled) 

![incremental deployment](./images/incremental-deployment.png "incremental deployment")

Duration of a deployment depends on the number of changes rather than the size of project.  For a typical CI/CD Pipeline that is triggered per commit, DataStage project deployments take a few minutes.

### Example Scenario

Consider this example CI/CD Pipeline

![ci cd pipeline](./images/cicd-pipeline-abstract.png "ci cd pipeline")

Using deployments with designs, this pipeline works as follows:

* Deploys to DataStage Projects that represent CI, SIT, QA and Prod environments
* Continuous Integration performed in the CI environment is 
    * Deployed from version control using Incremental Deployment
    * Runs automated Static Analysis and Unit Tests
    * Produces an release Artifact when successful
* Manual Testing/Verification is performed in SIT, QA and Prod environments
    * Deployed from release Artifact using Incremental Deployment
    * Manual tests could be replaced with automated tests

MettleCI’s [datastage deploy command](../../mettleci-cli/datastage-namespace/#datastage-deploy) would be used to perform the DataStage project deployments to the CI, SIT, QA and Prod environments.  In this scenario, the release Artifact will contain exactly the same ISX files as those checked out from Version Control for the purpose of Continuous Integration.  This is the recommended approach when building CI/CD Pipelines using MettleCI.

## Deployment of job binaries

Some customers have additional constraints or requirements which prevent the use of the job designs for deployments other than Continuous Integration. Typical examples are:

Compilers cannot be used in Production environments for security reasons

Only DataStage job binaries can be deployed to Testing and/or Production environments

While it is not the recommended approach for building CI/CD Pipelines using MettleCI, the following tools can be composed to perform DataStage project deployments with binaries.

### Incremental Export with binaries

MettleCI is designed so that ISX files checked into Version Control contain designs without binaries.  In order to get ISX files which include binaries, the source ISX files need to be first imported into a DataStage project, compiled and then exported to ISX with binaries.

A naïve approach would be implemented as follows:

1. Run a MettleCI Incremental Deployment using ISX files with designs
1. Export the entire DataStage project with binaries

The resulting export would have job designs which match the source ISX files while containing the required binaries.  Unfortunately, exporting an entire project is too slow and doesn’t scale well as the DataStage project increases in size.  A project with about 500 jobs will typically take about 45 minutes to export with binaries.

Instead, the DataStage project export can be performed by MettleCI’s [ISX export dommand](blank) which can optionally perform an incremental export with or without binaries.  Incremental Export reads from a DataStage project and exports its content into a  directory of ISX files.  If the export directory is empty then Incremental Export will export the entire DataStage project, otherwise only new or changed assets will be exported:

1. Source DataStage project and target export directory containing ISX files are analyzed for differences
1. Differences are converted to operations which update the ISX files in the target export directory 
1. When including binaries during export, an impact analysis of changes identified during step 2 is performed and all affected jobs are exported to capture the latest binaries (eg. a subflow component changed, so we export the binaries of all jobs which use it)

![incremental export](./images/incremental-export.png "incremental export")

Duration of export depends on the number of changes rather than the size of project.  For a typical CI/CD Pipeline that is triggered per commit, DataStage project exports take a few minutes.

### Incremental Import with binaries

An incremental import using the ISX Import Command is designed to accept a directory of ISX files and ensure that content of the target DataStage project will be updated to match the ISX files.  The process is very similar to an Incremental Deployment, the fundamental difference is that it doesn’t automatically compile jobs and is able to deploy binaries from the ISX files:

1. Source ISX files and the existing DataStage project are analyzed for differences
1. Differences are converted to operations which transform the existing DataStage project to match the source ISX files

Incremental Imports can also be configured to exclude design information.  When enabled, jobs will not be viewable/editable in the DataStage Designer/Flow Designer and any assets which are not required for execution (such as table definitions, shared containers, etc) will be excluded from the import.

### Example Scenario

Consider this example example CI/CD Pipeline

![ci cd pipeline](./images/cicd-pipeline-abstract.png "ci cd pipeline")

Using deployments with binaries, this pipeline works as follows:

* Deploys to DataStage Projects that represent CI, SIT, QA and Prod environments
* Continuous Integration performed in the CI environment is 
    * Deployed from version control
    * Runs automated Static Analysis and Unit Tests
    * Performs Incremental Export with binaries
    * Produces a release Artifact from exported binaries when Continuous Integration is successful
* Manual Testing/Verification is performed in SIT, QA and Prod environments
    * Deployed from release Artifact using Incremental Import
    * Manual tests could be replaced with automated tests

MettleCI’s [datastage deploy command](../../mettleci-cli/datastage-namespace/#datastage-deploy) is used to deploy the design only ISX files from Version Control.  When Continuous Integration completes successfully, ISX files with binaries are exported using the ISX Export Command  and an artifact is created from them.  All downstream deployments use the [isx import command](../../mettleci-cli/datastage-namespace/#datastage-deploy) to perform an incremental import of binaries, this process does not require a compiler.  Optionally, incremental import can be configured to ignore job designs while deploying to any environment.  This means that the SIT and QA environments could be deployed with designs and binaries while production is deployed with just binaries.

