## system version

![system version](img/system-version.svg "system version syntax")

The `system` namespace contains commands for understanding, diagnosing, and customizing your MettleCI CLI environment.  It can be useful in CI/CD pipelines as a diagnostic step to ensure the MettleCI CLI environment (terminal or container) is correctly configured. 

This command displays:

- The MettleCI CLI [command shell](../command-line/command-shell) version number,
- Your O/S version and architecture,
- Your O/S username and language/locale settings, and
- A list of MettleCI CLI plugins loaded from your `plugins` folder.

This command takes no parameters.

<details markdown="1">
  <summary>Example</summary>
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

---
