---
status: draft #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - Pipelines
---

# Asset Overlays

## What are Overlays?

Assets in your Development environment typically contain [hard coded](https://en.wikipedia.org/wiki/Hard_coding) references other development-specific assets, values and configurations. Overlays can be used to modify a variety of DataStage and non-DataStage asset types, including:

- **Jobs** ([documentation](https://dataplatform.cloud.ibm.com/docs/content/dstage/dsnav/topics/create-manage-jobs.html?context=cpdaas){:target="_blank" rel="noopener"}) - You can modify job properties, such as runtime parameters and configuration settings, to ensure that jobs run correctly in the target environment.
- **Local parameters** ([documentation](https://dataplatform.cloud.ibm.com/docs/content/dstage/dsnav/topics/creating_parameters.html?context=cpdaas){:target="_blank" rel="noopener"}),
- **DataStage Parameter Sets**, **Value Sets**, and **Value Set Files** ([documentation](https://dataplatform.cloud.ibm.com/docs/content/dstage/dsnav/topics/create-and-use-parameter-sets.html?context=cpdaas){:target="_blank" rel="noopener"}) - You can use overlays to change the values of parameters in a Parameter Set, allowing you to adapt the behavior of DataStage Jobs and Flows for different environments.
- **Data Connections** ([documentation](https://dataplatform.cloud.ibm.com/docs/content/dstage/dsnav/topics/datastage-connectors.html?context=cpdaas){:target="_blank" rel="noopener"}) - Overlays can be used to update connection details, such as database hostnames, usernames, and passwords, enabling DataStage assets to connect to the appropriate data sources in each environment.
- **Non-DataStage assets** - Ovelays can also be used to adapt non-DataStage assets, such as **Filesystem scripts** and **Configuration files** used alongside your DataStage Jobs and Orchestration Pipelines.

Deploying these assets into downstream environments, such as Test and Production, can be challenging as the deployment process requires adapting these Development environment-specific values/references to those that will allow the asset to behave correctly in the target environment.  This process of adaption needs to be fast, accurate, repeatable, and traceable, and is ideally implemented as an automation step in your CI/CD pipeline. This automation capability is provided in DataStage NextGen by the **MettleCI Overlays** feature, and is accessed using the MettleCI command line's ([mcix overlay apply](../command-ref/overlay-namespace)) command.





## How Overlays work

Overlays are implemented by taking one or more DataStage NextGen export files and modifying them using the `mcix overlay apply` command ([documentation](http://nextgen.mettleci.io/mettleci-cli/overlay-namespace/#overlay-apply)).  This command takes its parameters from one or more text configuration files provided in one of two formats:

1. Overlay files in [json5](https://json5.org/){:target="_blank" rel="noopener"} format, or
2. Properties files in key/value format.

These configuration files specify the changes that need to be applied to the DataStage assets in order to adapt them for the target environment.  The `mcix overlay apply` command reads the specified configuration files and applies the defined changes to the relevant DataStage assets, producing a new set of modified assets which are then deployed to the target environment.













## Where to use Overlays

You can use the `mcix overlay apply` command in a number of contexts - even manually if that's how you wish to perform your deployments - but the ideal application of overlays is within the context of a build and deployment pipeline implemented in your chosen CI/CD tool (Jenkins, GitHub Actions, Azure DevOps, etc.) 


In this context, the typical process (demonstrated  the example pipelines available [here](https://github.com/MettleCI){:target="_blank" rel="noopener"}) is as follows: 

1. Commit your Development-specific assets from your development environment (DataStage NextGen) which will trigger your configured CI/CD pipeline.
2. The CI/CD pipeline checks out the committed Development-specific assets into a working directory then runs the `mcix overlay apply` command (or native task - see below) to apply a set of 'overlays' for the target environment (CI, Test, Prod, etc.)
3. The modified assets are then deployed to the target environment (DataStage NextGen project)
 

This process uses the `mcix overlay apply` command (or, in supported build tools, the `mcix overlay apply` build action/task - [REFERENCE HERE](../mcix-build-tasks)) to apply the overlays which modify the Development-specific assets into target environment-specific assets.

For example, a typical CI process will respond to a Git commit by triggering a pipeline which will take the repository contents, move it into a working directory and running `mcix overlay apply` for a nominated target environment ('CI', in this case).  The `mcix overlay apply` command will look for the relevant overlay files defined in your repository and apply them by substituting the specified values in the specified assets. This modified set of assets will then be deployed to the relevant CI project after which your CI pipeline’s other processes will be performed - typically running flow analysis and unit tests.

Once CI has completed successfully you can then invoke (either manually, or automatically) a subsequent deployment process for another environment (testing or production) which will also use the `mcix overlay apply` command to perform the same asset customization process using a set of overlays files for that target environment.











When you deploy this development-specific release to a different environment, the `mcix overlays apply` command will reference a set of values you have defined and apply them to the relevant assets in your release to dynamically generate a new, target environment-specific version of that release.  

This can also include environment runtime parameters, such as the name of the DataStage engine and workload queue upon which the jobs should be executed.

The environment-specific assets you supply are the 'overlays' which are simple text files (format below) which should ideally be themselves stored in Git

Parameters for input assets and output assets can specified either as a zip file or a directory of assets.






You can use the `mcix overlay apply` command in any context - even manually if you so desire:

```bash

# Export from DataStage NextGen to a local directory called ./datastage, then ...

# Apply overlays for the target environment
mcix overlay apply \
  -assets "./datastage" \
  -output "./build/deployment.zip" \
  -overlay "./overlays/${TARGET_ENVIRONMENT}"

# Deploy to the relevant DataStage NextGen project...
mcix datastage import \
  -url "${CPD_HOST}" -user "${CPD_USER}" -api-key "${CPD_PASSWORD}" \
  -project "${CPD_PROJECT}" \
  -assets "./build/deployment.zip"

# ... and compile to prepare the assets for execution
mcix datastage compile \
  -url "${CPD_HOST}" -user "${CPD_USER}" -api-key "${CPD_PASSWORD}" \
  -project "${CPD_PROJECT}" \
  -report "./build/compile.junit.xml"
```






## Project Structure

A typical MCIX project is organized into two main sections:

- DataStage assets: Contains the base DataStage assets committed by developers or it could be a project export zip, and
- Overlay Directories: Contains environment-specific folders where you can adjust the base DataStage assets using additional configuration files.

Here's an example directory structure:

```
┆
├── datastage/
│   ├── connection/
│   │   └── database.json
│   ├── data_intg_flow/
│   │   ├── extract.json
│   │   ├── transform.json
│   │   └── load.json
│   ├── job/
│   │   ├── extract.DataStage job.json
│   │   ├── transform.DataStage job.json
│   │   └── load.DataStage job.json
│   ├── orchestration_flow/
│   │   └── batch.json
│   ├── parameter_set/
│   │   └── common_parameters.json
│   └── DataStage-README.json
├── overlays/
┆   ├── test/
    ├── qa/
    └── prod/
```











### DataStage Assets

DataStage assets contain exported CPD assets that are included in a release. This can be a directory
structure containing assets committed from CPD into a Git repository or a whole project export zip.
When defining these assets, they can be committed/exported directly from their source CPD project,
no environment-specific settings like database host and user names need to be modified. These
assets provide the “base” of your release, to which overlays are applied, producing an environment-
specific variation which is then deployed.

### Overlays

An overlay is a directory containing configuration files which are used to update DataStage assets
with environment-specific settings. For example, changing Parameter Set values or Job parameters.

The following asset types can be updated using overlays

- Parameter Sets
- Connections
- Jobs

All overlay configuration files are in JSON5 format (https://json5.org/), which is essentially JSON but with additional support for comments and optional quoting for property names.

Overlay files can be stored in any location you wish, however a good convention (and the convention employed by ) would be to store overlay files in a top-level folder structure which mirrors, somewhat, the structure of your top level `datastage` folder. i.e. 

```
{repository_root} / overlays / {environment} / {asset-type} / {asset_name}.json5
```

For example, the following file in your Git repository ...

`myProject/datastage/parameter_set/common_parameters.json`

... would be modified by the values in the following overlay file when being deployed to your CI project:
  
`myProject/overlays/ci/parameter_set/common_parameters.json5`

... and by the values in this overlay file when deployed to your PROD project:

`myProject/overlays/prod/parameter_set/common_parameters.json5`





















## Overlay examples

### A Test environment parameter set

Applying an overlay for a test environment may typically involve changing a `common_parameters` parameter set
so that the default `inputDir` and `outputDir` parameter values refer to the correct directories for testing.
You could, for example, add a `common_parameters` configuration file to the `overlays/test/parameter_set` directory:

```
┆
└── overlays/
    ├── test/
    │   └── parameter_set/
    │       └── common_parameters.json5
    ├── qa/
    └── prod/
```

In the newly created `common_parameters.json5` file, define the updated values for `inputDir` and `outputDir`:

```
{
  inputDir: "/test/input",
  outputDir: "/test/output",
}
```

In this case our overlay configuration file does not need to define an entry for every parameter in the
`common_parameters` parameter set - you only need to define the parameters which are being modified by this overlay. 

### A Quality Assurance environment database connection

In addition to setting QA specific parameter set values, your QA environment may also need updating with different
Database credentials, for example. This is done by adding a database configuration file to the `overlays/qa/connection` directory:

```
┆
└── overlays/
    ├── test/
    │   └── ...
    ├── qa/
    │   ├── connection/
    │   │   └── database.json5
    │   └── parameter_set/
    │       └── common_parameters.json5
    └── prod/
```

Alongside a QA specific version of `common_parameters.json5`, define the following `database.json5` file to update the connection details of the database connection:

```
{
  oracle_db_host: "qa.database.local",
  oracle_service_name: "qa",
  username: "scott",
  password: "${DATABASE_PASSWORD}",
}
```

The connection properties that can be set using an overlay depends on the type of connection being used. 
This example changes the database host, instance, username and password for a DataStage Oracle Connection. 
Variables such as `${DATABASE_PASSWORD}` are substituted from either environment variables or a **separate 
property file passed to the mcix overlay command** - more details on this are covered in later sections. 
Substitutions like this allows parameters to be provided externally from your CI/CD Pipeline or setting sensitive credentials
without needing to store them in Git.

???+ info "Note"

    Note that **Data Connections** in NextGen don't support Parameter Sets like those in DataStage Classic as their values are 'baked in' at compilation
    time. Adapting Data Connections for different environments therefore requires that the altered asset be re-compiled after deployment.

### A Production environment job configuration

In your Production environment you may want to customize not only the parameter set and connection details as
described in the previous examples, but also the properties used when running Jobs. This may include changing 
the warning limit to `0`, for example, so that a DataStage job fails if it produces any warnings, or setting an
environment variable parameter for the Flow.  To do this you would define a new overlay configuration file in
the `overlays/prod/job` directory which, for this example, we'll call `transform.DataStage-job.json5`:

```
┆
└── overlays/
    ├── test/
    │   └── ...
    ├── qa/
    │   └── ...
    └── prod/
        ├── connection/
        │   └── database.json5
        ├── job/
        │   └── transform.DataStage-job.json5
        └── parameter_set/
            └── common_parameters.json5
```

The job configuration file defines an overlay which modifies both the job configuration as well as parameter values:

```
{
  configuration: {
    flow_limits: {
      warn_limit: 0
    },
    job_parameters: {
      "$APT_RECORD_COUNTS": true
    }
  }
}
```