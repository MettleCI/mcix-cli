## system version

[<img src="https://img.shields.io/badge/github-marketplace-blue?style=flat-square&logo=github">](https://github.com/marketplace/actions/mcix-system-version){:target="_blank" rel="noopener"} 

This command displays:

- The MettleCI CLI [command shell](../command-line/command-shell) version number,
- Your O/S version and architecture,
- Your O/S username and language/locale settings, and
- A list of MettleCI CLI plugins loaded from your `plugins` folder.

This command takes no parameters.

<details markdown="1">
  <summary>Example</summary>
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

---
