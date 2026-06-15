---
title: MCIX CLI Plugins
description: The framework for providing MCIX capabilities   
# banner_src: ./img/carbon-header.png
---

# MCIX CLI Plugins

## CLI Structure

The MettleCI Command Line Interface for DataStage NextGen (MCIX) comprises a [Command Shell](command-shell) which provides a command line interface into a set of MettleCI CLI Plugins (supplied as a set of `.jar` files) which provide MCIX with its capabilities.

![MCIX architecture](./img/mcix-command-shell.png "MCIX architecture")

The MettleCI Command Shell is used to execute the commands made available by the installed CLI plugins. Each command exists within a Namespace which is required to fully qualify the required command. The compliance and unittest namespaces, for example, both feature a test command, each of which perform unrelated functions. The Command Shell is used like this:

```
# Windows
C:\> mettleci.cmd {namespace} {command} {parameters} 
```

```
# UNIX
$> mettleci {namespace} {command} {parameters}

# e.g.
$> mettleci datastage deploy \
   -domain services-tier.myorg.com:59445 -server engine-tier.myorg.com  \
   -project dstage1 \
   -username isadmin -password isadminpwd \
   -assets assets_dir
   -include-job-in-test-name
```

## Directory Structure

The MettleCI CLI directory structure looks like this. Plugins are supplied as .jar files which are installed in the plugins directory.

```
.
├── bin
│   └── <implementation>.jar
├── config.properties
├── docs
│   ├── namespace1
│   │   ├── <command1-documentation>
│   │   ├── <command2-documentation>
│   │   ├── <command3-documentation>
│   │   └── <command4-documentation>
│   ├── namespace2
│   │   ├── <command1-documentation>
│   │   └── <command2-documentation>
│   ├── namespace3
│   │   ├── <command1-documentation>
│   │   ├── <command2-documentation>
│   │   └── <command4-documentation>
├── lib
│   └── <implementation>.jar
├── log
├── mettleci
├── mettleci.cmd
└── plugins
    ├── <filename1>-plugin-<major-version>-<build-number>.jar
    ├── <filename2>-plugin-<major-version>-<build-number>.jar
    ├── <filename3>-plugin-<major-version>-<build-number>.jar
    └── <filename4>-plugin-<major-version>-<build-number>.jar
```

### Available Commands

Details about the namespaces and commands currently available in MettleCI are available here.