---
title: Local development
---

## Set up environment

This repository uses [dev containers](http://containers.dev/) to avoid version
conflicts between the base system and the repository's dependencies (ruby,
jekyll). Dev containers require a docker daemon to be running. The easiest
[IBM-approved](https://w3.ibm.com/w3publisher/docker-desktop/rancher-desktop)
way to do so is to to use Rancher Desktop.

1. [Install Rancher Desktop](https://rancherdesktop.io) for your system
2. Open Rancher Desktop → Preferences
3. Set "Container Engine" to "dockerd (moby)" and apply
4. In "Kubernetes", you can uncheck the "Enable Kubernetes" checkbox (optional)
5. Install the
   [official "Dev containers"](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
   VS Code extension
6. Whenever you open this repository in VS Code, you should receive a
   notification to "Reopen in container". Should you not see this, click on the
   left-bottom-most icon (<sub>&gt;</sub><sup>&lt;</sup>) and select "Reopen in
   container".

The first time will take a while to download, but any subsequent opening should
be fast.

**Please note:** Rancher Desktop must be running in order for you to connect to
the dev container.

## Run locally

In your [dev container](#set-up-environment), running the following command will
serve the page locally at [localhost:4000](http://localhost:4000):

```console
jekyll serve --livereload
```

**Please note:** After any modification to `_config.yml`, you must stop the dev
server and run above command again.

## Build locally

In your [dev container](#set-up-environment), running the following command will
build all pages and produce the static `_site` directory.

```console
jekyll build
```
