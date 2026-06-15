---
title: "Asset Overlays&nbsp; Detailed Examples"
description: Extending Overlays to more complex scenarios
# order: 3
# banner_src: ../assets/img/carbon-header.png
---

## Adding, modifying and removing Parameter Set Value files

Overlays are not limited to updating the values in default parameter set values. 
They can also be used to modify or even add new parameter set value files. 

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

To add a new parameter set value file called performance_testing.json5 , follow the 
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

The examples use a single overlay per environment but mcix overlay allows the application of
multiple overlays when generating the environment specific releases. It also allows variable
substitutions from both environment variables and properties file.

**In the examples above**, environment-specific overlays have been used. This would be achieved 
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

The `mcix overlay apply` (documentation) command is not restricted to applying a single overlay. 
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

