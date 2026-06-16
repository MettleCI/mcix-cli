---
status: draft #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - Pipelines
---

# Overlay examples

## A Test environment parameter set

Applying an overlay for a test environment may typically involve changing a `common_parameters` parameter set
so that the default `inputDir` and `outputDir` parameter values refer to the correct directories for testing.
You could, for example, add a `common_parameters` configuration file to the `overlays/test/parameter_set` directory:

```
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

## A Quality Assurance environment database connection

In addition to setting QA specific parameter set values, your QA environment may also need updating with different
Database credentials, for example. This is done by adding a database configuration file to the `overlays/qa/connection` directory:

```
└── overlays/
    ├── test/
    │   └── parameter_set/
    │       └── common_parameters.json5
    ├── qa/
    │   ├── connection/
    │   │   └── database.json5
    │   └── parameter_set/
    │   └── common_parameters.json5
    └── prod/
```

Alongside a QA specific version of `common_parameters.json5`, define the following`database.json5` file to update the connection details of the database connection:

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

## A Production environment job configuration

In your Production environment you may want to customize not only the parameter set and connection details as
described in the previous examples, but also the properties used when running Jobs. This may include changing 
the warning limit to 0, for example, so that a DataStage job fails if it produces any warnings, or setting an
environment variable parameter for the Flow.  To do this you would define a new overlay configuration file in
the `overlays/prod/job` directory which, for this example, we'll call `transform.DataStage job.json5`:

```
└── overlays/
    ├── test/
    │   └── parameter_set/
    │   └── common_parameters.json5
    ├── qa/
    │   ├── connection/
    │   │ └── database.json5
    │   └── parameter_set/
    │   └── common_parameters.json5
    └── prod/
        ├── connection/
        │   └── database.json5
        ├── job/
        │   └── transform.DataStage job.json5
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