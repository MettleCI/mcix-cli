## system version

![system version](img/system-version.svg "system version syntax")

This command displays:

- The MettleCI CLI [command shell](../command-shell/command-shell) version number,
- Your O/S version and architecture,
- Your O/S username and language/locale settings, and
- A list of MettleCI CLI plugins loaded from your `plugins` folder.

This command takes no parameters.

#### Examples

<details markdown="1">
  <summary>Command Line</summary>
```shell
{% raw %}# mcix system version
mcix system version
{% endraw %}```

Example output is ...

```shell
MettleCI Command Line (build 1.0-123)
(C) 2018-2025 Data Migrators Pty Ltd
system version (1.0-123)
Mac OS X 26.0 (aarch64)
johnmckeever, English (Australia)

Loaded plugins:
* MettleCI CP4D Asset-Analysis Plugin (1.0-123)
* MettleCI CP4D Compilation Plugin (1.0-456)
* MettleCI CP4D Import Plugin (1.0-789)
* MettleCI CP4D Overlays Plugin (1.0-012)
```
</details>

<details markdown="1">
  <summary>GitHub Actions</summary>
```yaml
{% raw %}# mcix system version
- name: mcix system version action
  uses: mettleci/mcix/system/version@latest
  id: mcix-system-version
{% endraw %}```

This will produce a GitHub Actions step summary of the form...

```
MettleCI Command Line (build 1.0-94)
(C) 2018-2026 Data Migrators Pty Ltd
system version (1.0-94)
Linux 6.14.0-1017-azure (amd64)
root, English (United States)

▶ Image compliance information

▶ GitHub execution environment

▶ MCIX plugins loaded
```

... where the expandable sections provide extra information:

- **Image compliance information** lists the compliance status of the MettleCI CLI container image,
- **GitHub execution environment** lists details of the GitHub-hosted runner executing the command, and 
- **MCIX plugins loaded** lists all MettleCI CLI plugins provided by the `mcix` command.
</details>

<details markdown="1">
  <summary>Azure DevOps Task</summary>
```yaml
{% raw %}# mcix system version
- task: mcixSystemVersion@1
  displayName: mcix system version action
  inputs:
    imageName: 'your.registry.com/namespace/mcix'
{% endraw %}```

THis will produce a task log output of the form...

```
███╗   ███╗███████╗████████╗████████╗██╗     ███████╗ ██████╗██╗
████╗ ████║██╔════╝╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║
██╔████╔██║█████╗     ██║      ██║   ██║     █████╗  ██║     ██║
██║╚██╔╝██║██╔══╝     ██║      ██║   ██║     ██╔══╝  ██║     ██║
██║ ╚═╝ ██║███████╗   ██║      ██║   ███████╗███████╗╚██████╗██║
╚═╝     ╚═╝╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝ ╚═════╝╚═╝
MettleCI DevOps for DataStage       (C) 2021-2026 Data Migrators

/usr/share/mcix/bin/mcix system version
MettleCI Command Line (build 1.0-94)
(C) 2018-2026 Data Migrators Pty Ltd
system version (1.0-94)
Linux 6.14.0-1017-azure (amd64)
root, English (United States)

Loaded plugins:
* MettleCI CP4D Asset Analysis Plugin (2.1-309)
* MettleCI CP4D Compile Plugin (1.0-84)
* MettleCI CP4D Export Plugin (1.0-34)
* MettleCI CP4D Import Plugin (1.0-102)
* MettleCI DataStage Classic to CP4D Migration Plugin (1.0-150)
* MettleCI CP4D Overlays Plugin (1.0-9)
* MettleCI CP4D Unit Testing Plugin (1.0-91)

▶ Image compliance information
```

The **MCIX plugins loaded** section lists all MettleCI CLI plugins provided by the `mcix` command and the expandable 
**Image compliance information** section lists the compliance details of the MettleCI CLI container image .
</details>

<details markdown="1">
  <summary>Jenkins</summary>
```yaml
{% raw %}# mcix system version
stage("Diagnostics") {
    agent {
        docker {
            registryUrl 'https://ghcr.io'
            registryCredentialsId 'GHCR'
            image 'ghcr.io/mettleci/mcix:latest'
            args "-u root --entrypoint=''"
        }
    }
    steps {
        mcixSystemVersion()
    }
  }
{% endraw %}```
</details>

