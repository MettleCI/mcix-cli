---
status: reviewed #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - Pipeline
  - CLI
---
# system namespace

The `system` namespace contains commands for understanding, diagnosing, and customizing your MettleCI CLI environment.  It can be useful in CI/CD pipelines as a diagnostic step to ensure the MettleCI CLI container environment is correctly configured. 

## system version

![system version](../railroads/svgs/system-version.svg "system version syntax")

This command displays:

- The MettleCI CLI [command shell](../command-shell) version number,
- Your O/S version and architecture,
- Your O/S username and language/locale settings, and
- A list of MettleCI CLI plugins loaded from your `plugins` folder.

#### Examples

=== "Command Line"
    ```shell
    mcix system version
    ```

    Example output is ...

    ```shell
    MettleCI Command Line (build 1.0-123)
    (C) 2018-2025 Data Migrators Pty Ltd
    system version (1.0-123)
    Mac OS X 26.0 (aarch64)
    johnmckeever, English (Australia)

    Loaded plugins:
    * MettleCI CP4D Asset-Analysis Plugin (1.0-SNAPSHOT)
    * MettleCI CP4D Compilation Plugin (1.0-SNAPSHOT)
    * MettleCI CP4D Import Plugin (1.0-SNAPSHOT)
    * MettleCI CP4D Overlays Plugin (1.0-SNAPSHOT)
    ```

=== "GitHub Action"
    ```yaml
    - name: mcix system version action
      uses: mettleci/mcix/system/version@latest
      id: mcix-system-version
    ```

    This will produce a step summary of the form...

    #### MCIX System Version

    ```
    MettleCI Command Line (build 1.0-94)
    (C) 2018-2026 Data Migrators Pty Ltd
    system version (1.0-94)
    Linux 6.14.0-1017-azure (amd64)
    root, English (United States)
    ```

    ▶ Image compliance information

    ▶ GitHub execution environment

    ▶ MCIX plugins loaded

    ... where the expandable sections provide extra information:
    
    - "Image compliance information" lists the compliance status of the MettleCI CLI container image,
    - "GitHub execution environment" lists details of the GitHub-hosted runner executing the command, and 
    - "MCIX plugins loaded" lists all MettleCI CLI plugins provided by the `mcix` command.

=== "Azure DevOps Task"
    ```yaml
    - task: mcixSystemVersion@1
      inputs:
        imageName: 'mettleci.azurecr.io/mettleci/mcix'
      displayName: mcix system version action
    ```

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

    The "MCIX plugins loaded" section lists all MettleCI CLI plugins provided by the `mcix` command and the expandable 
    "Image compliance information" section lists the compliance details of the MettleCI CLI container image .

---
