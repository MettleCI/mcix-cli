---
title: Asset Overlays
description: Automatically preparing assets for deployment to target environments
# order: 3
# banner_src: ../assets/img/carbon-header.png
---

## What are Asset Overlays?

Assets in your Development environment typically contain [hard coded](https://en.wikipedia.org/wiki/Hard_coding) references other development-specific assets, values and configurations. Deploying these assets into downstream environments, such as QA and Production, can be challenging as the deployment process needs to adapt these Development environment-specific values/references to those that will allow the asset to behave correctly in the target environment.  

This process of adaption needs to be fast, accurate, repeatable, and traceable, and is ideally implemented as an automation step in your CI/CD pipeline. This automation capability is provided in DataStage NextGen by the **MCIX Overlays** feature, and is accessed using the MettleCI command line's ([mcix overlay apply](../command-ref/overlay-namespace)) command.

Overlays can be used to modify a variety of DataStage and non-DataStage asset types, including:

- **Jobs** ([documentation](https://dataplatform.cloud.ibm.com/docs/content/dstage/dsnav/topics/create-manage-jobs.html?context=cpdaas){:target="_blank" rel="noopener"}) - You can modify job properties, such as runtime parameters and configuration settings, to ensure that jobs run correctly in the target environment.
- **Local parameters** ([documentation](https://dataplatform.cloud.ibm.com/docs/content/dstage/dsnav/topics/creating_parameters.html?context=cpdaas){:target="_blank" rel="noopener"}),
- **DataStage Parameter Sets**, **Value Sets**, and **Value Set Files** ([documentation](https://dataplatform.cloud.ibm.com/docs/content/dstage/dsnav/topics/create-and-use-parameter-sets.html?context=cpdaas){:target="_blank" rel="noopener"}) - You can use overlays to change the values of parameters in a Parameter Set, allowing you to adapt the behavior of DataStage Jobs and Flows for different environments.
- **Data Connections** ([documentation](https://dataplatform.cloud.ibm.com/docs/content/dstage/dsnav/topics/datastage-connectors.html?context=cpdaas){:target="_blank" rel="noopener"}) - Overlays can be used to update connection details, such as database hostnames, usernames, and passwords, enabling DataStage assets to connect to the appropriate data sources in each environment.
- **Non-DataStage assets** - Ovelays can also be used to adapt non-DataStage assets, such as **Filesystem scripts** and **Configuration files** used alongside your DataStage Jobs and Orchestration Pipelines.

## How Overlays work

Overlays are implemented by taking one or more DataStage NextGen export files on your filesystem and modifying them using the `mcix overlay apply` command ([CLI documentation](/command-line/command-reference#overlay-apply)) or task (if you're using a CI/Cd tool.)  The `mcix overlay apply` command accepts parameters from one or more text configuration files and applies the changes defined in those files to the specified DataStage assets, producing a set of modified assets in your filesystem which are then ready for deployment to the target environment.

We'll look at a practical example focussing on two directories a DataStage project repository:

```
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
│   └── parameter_set/
│       └── common_parameters.json
├── filesystem
├── pipelines
└── overlays/
    ├── ci/
    ├── qa/
    └── prod/
```

The important directories are:

- `datastage` - Contains the 'base' (unmodified) DataStage assets from your Development environment 
- `overlays` - Contains environment-specific folders with configuration files describing the modifications requried to your DataStage assets required for each environment 

Overlay files can be stored in any location you wish, however best practice is to store overlay files in a top-level folder structure which mirrors, somewhat, the structure of your top level `datastage` folder. i.e. 

```
/ overlays / {environment} / {asset-type} / {asset_name}.json5
```

Here are some overlay files which will enable us to modify the exported development
parameter set `common_parameters.json` to be usable on the CI, QA and Prod environments:

```
├── datastage/
│   ├── connection/
│   ├── data_intg_flow/
│   ├── job/
│   ├── orchestration_flow/
│   └── parameter_set/
│       └── common_parameters.json
├── overlays/
│   ├── ci/
│   │   └── common_parameters.json5
│   ├── qa/
│   │   └── common_parameters.json5
│   └── prod/
│       └── common_parameters.json5
```

The `mcix overlay apply` command accepts configuration files in [json5](https://json5.org/){:target="_blank" rel="noopener"} format, described in the examples below.  The command also accepts properties files using a simpler key/value format, but this format provides less flexibility and is not recommended for new projects.

## Overlay examples

You can use the `mcix overlay apply` command in a number of contexts - even manually if that's how you wish to perform your deployments - but the ideal application of overlays is within the context of a build and deployment pipeline implemented in your chosen CI/CD tool (Jenkins, GitHub Actions, Azure DevOps, etc.) 

The command parameters specifying DataStage source assets, and the output assets produced by the `mcix overlay apply` command, can specified either as a zip file or a directory of assets.  Here's an example of applying a 'CI' overlay to a directory of DataStage assets and generating a deployable zip file of modified assets:

```bash
# Export from DataStage NextGen to a local directory called ./datastage, then ...

# Apply overlays for the target CI environment
mcix overlay apply \
  -assets "./datastage" \
  -output "./build/deployment.zip" \
  -overlay "./overlays/CI"

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

<cds-inline-notification
  kind="info"
  title="Note"
  subtitle="Data Connections in NextGen don't support Parameter Sets like those in DataStage Classic as their values are 'baked in' at compilation
    time. Adapting Data Connections for different environments therefore requires that the altered asset be re-compiled after deployment."
  low-contrast
  hide-close-button="true"
  id="overlay-notification">
</cds-inline-notification>

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

---


## Manipulating Parameter Set Value files

Overlays are not limited to updating the values in default parameter set values. They can 
also be used to modify or even add new parameter set value files. 

For example, to modify an existing parameter set value file called `unit_testing` 
for the `common_parameters` parameter set in the test overlay, add a new
`unit_testing.json5` file in the `/overlays/test/parameter_set/common_parameters/`
folder:

```
└── overlays/
    ├── test/
    │   └── parameter_set/
    │   ├── common_parameters/
    │   │ └── unit_testing.json5
    ┆   └── common_parameters.json5
```

Like the previous examples, the `unit_testing.json5` file contains just the entries 
that you wish to change within the unit_testing value file.

To add a new parameter set value file called `performance_testing.json5` , follow the 
same procedure but ensure the configuration file contains every non-default parameter:

```
└── overlays/
    ├── test/
    │   └── parameter_set/
    │   ├── common_parameters/
    │   │ ├── performance_testing.json5
    │   │ └── unit_testing.json5
    ┆   └── common_parameters.json5
```

The unit_testing value file for `common_parameters` might be included as part of DataStage
assets export files in `/datastage/` but you may want to remove it when deploying to production.
This can be configured by adding a `unit_testing.json5` file to `/overlays/prod/parameter_set/common_parameters/`. 
For example:

```
└── overlays/
    ├── test/
    │   └── parameter_set/
    │   ├── common_parameters/
    │   │   ├── performance_testing.json5
    │   │   └── unit_testing.json5
    │   └── common_parameters.json5
    ├── qa/
    │   ├── connection/
    │   │   └── database.json5
    │   └── parameter_set/
    │       └── common_parameters.json5
    └── prod/
        └── parameter_set/
            ├── common_parameters/
            │    └── unit_testing.json5
            └── common_parameters.json5
```

Instead of configuring `/overlays/prod/parameter_set/common_parameters/unit_testing.json5` with the 
parameters you want changed for your production environment, set its content to `null`.

```
null
```

When applying this overlay configuration, the `unit_testing` parameter set value file will be 
removed entirely.

## Flexibility in Directory Structure

The examples use a single overlay per environment but the `mcix overlay apply` operation allows the 
application of multiple overlays when generating the environment specific releases. It also allows 
variable substitutions from both environment variables and properties file.

In the examples given above, environment-specific overlays have been used. This would be achieved 
by running ...

```
mcix overlay apply \
    -assets ./datastage \
    -overlay ./overlays/<environment> \
    -output release.zip
```

... where `<environment>` represents the name of the environment being deployed.

If every environment requires the same configuration changes but with different values, it is possible
to use a single overlay and rely on variable substitution for setting the values. For example,
instead of having a `database.json5` overlay file for each environment, a single common overlay
could be used along with environment specific variable substitution file:

```
├── datastage/
│   └── ...
├── overlays/
│   └── common/
│       └── connection/
│           └── database.json5
├── test.var
├── qa.var
└── prod.var
```

The `database.json5` file would then look like this:

```
{
    oracle_db_host: "${database.host}",
    oracle_service_name: "${database.instance}",
    username: "${database.username}",
    password: "${database.password}",
}
```

The variables for each environment can be specified in the `test.var`, `qa.var`, and `prod.var` files.

The following is an example of the variables stored in `qa.var` :

```
database.host = qa.database.local
database.instance = qa
database.username = scott
database.password = tiger
```

This would then be executed like this ...

```
 mcix overlay apply \
   -assets ./datastage
   -overlay ./overlays/common \
   -properties qa.var \
   -output release.zip
```

The `mcix overlay apply` command ([documentation](/command-line/command-reference#overlay-apply)) is not restricted to applying a single overlay. 
This also allows the above strategies to be combined:

```
├── datastage/
│   └── ...
├── overlays/
│   ├── common/
│   ├── test/
│   ├── qa/
│   └── prod/
├── test.var
├── qa.var
└── prod.var
```

This approach would be executed like this ...

```
mcix overlay apply \
   -assets ./datastage \
   -overlay ./overlays/common \
   -overlay ./overlays/<environment> \
   -properties qa.var \
   -output release.zip
```

... where `<environment>` again represents the name of the environment being deployed.

