---
title: The MCIX Container
description: MCIX capabilities packaged as an<br/>OCI-compliant Docker container image
# banner_src: ../../assets/img/banner.jpeg
---

<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/card-group.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block-mixed.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/link-list.min.js"></script>

<c4d-link-list type="default" slot="complementary">
  <c4d-link-list-heading>Resources</c4d-link-list-heading>
  <c4d-link-list-item
    href="https://github.com/marketplace?query=mcix"
    target="github-marketplace"
    cta-type="external"
  >
    MCIX Container
  </c4d-link-list-item>
</c4d-link-list>

## Introduction

The MCIX container image is currently available in the following registries:

| Platform  | Registry URL |
|-----------|--------------|
| Azure     | mettleci.azurecr.io/mettleci/mcix |
| DockerHub | mettleci/mcix |
| GitHub    | ghcr.io/mettleci/mcix:latest |
| IBM       | icr.io/mettleci/mcix |

Retrieve the MCIX container image using the [`docker pull`](https://docs.docker.com/reference/cli/docker/image/pull/){:target="_blank" rel="noopener"} 
command then use [`docker run`](https://docs.docker.com/reference/cli/docker/container/run/){:target="_blank" rel="noopener"} to invoke MCIX commands 
within a container instance of the image. 

<cds-inline-notification
  kind="info"
  title="Note"
  subtitle="If required, you can pull the MCIX container image from a public location and re-host it in your own private container registry."
  low-contrast
  id="overlay-notification">
</cds-inline-notification>

<!--
<cds-inline-notification
  kind="warning"
  title="Files created inside the container are temporary"
  low-contrast="true"
  hide-close-button="true">
  <div class="cds--inline-notification__subtitle">
    <p>Files written inside the container will be lost when the container exits.
       Mount a host directory using <code>-v host_path:container_path</code>.</p>
    <p>See the <a href="./running-mcix-in-containers.html">container usage guide</a>
      for a complete example.</p>
  </div>
</cds-inline-notification>
-->

## Basic example

Here's a simple example of how to call `mcix datastage import` inside an instance of the MCIX container using `docker run`. 
The `--rm` flag in the docker run command instructs Docker to automatically remove the container and its file system once it exits.

```
docker run --rm                     \
  ghcr.io/mettleci/mcix:latest      \
  mcix datastage export             \
    -url "https://cpd.example.com"  \
    -user "my-user"                 \
    -api-key "my-api-key"           \
    -project "My DataStage Project" \
    -assets "/export"
```

## Mount a local filesystem

Many MCIX commands generate output files, such as JUnit test results. By default, these files exist only inside the container and are 
lost when the container exits. To preserve files created by MCIX commands, use the `docker run -v` (or `--volume`) flag to mount a 
host directory into the container.  The volume argument takes the form `host_path:container_path`.  Make sure the path you mount in 
the container is the same directory you specify as the output directory in your MCIX command.

The example below mounts the host's' `./my_assets` directory into the container at `/export`. The MCIX command then writes exported 
assets to `/export`, ensuring they remain available in the host’s `./my_assets` directory after the container exits.

```
docker run --rm                     \
  -v "$PWD/my_assets:/export"       \
  ghcr.io/mettleci/mcix:latest      \
  mcix datastage export             \
    -url "https://cpd.example.com"  \
    -user "my-user"                 \
    -api-key "my-api-key"           \
    -project "My DataStage Project" \
    -assets "/export"
```

## Invoke multiple commands

You can run multiple commands within a single instance of the container by using `docker run` to invoke a shell (`sh`) within the container 
and passing your MCIX commands as an inline script to the shell process using the `sh -c` parameter.

When calling multiple MCIX commands you are likely to find yourself repeating parameters across commands, particularly authentication credentials.  
This example uses the `-e` (or `--env`) flag to set environment variables once inside the running container which can then be referenced 
consistently across all commands.

This example also mounts multiple host directories into the container to suit different output types. 

```
docker run --rm                                     \
  --entrypoint /bin/sh                              \
  -v "$PWD/project:/workspace/project"              \
  -v "$PWD/overlays:/workspace/overlays"            \
  -v "$PWD/results:/workspace/results"              \
  -e CPD_URL="https://cpd.example.com"              \
  -e CPD_USER="my-user"                             \
  -e CPD_APIKEY="my-api-key"                        \
  ghcr.io/mettleci/mcix:latest                      \
  -c '                                              \
    set -e                                          \
                                                    \
    echo "Applying overlay..."                      \
    mcix overlay apply                              \ 
      --source /workspace/project                   \
      --overlay /workspace/overlays/dev             \
      --target /workspace/project-overlayed         \
                                                    \
    echo "Importing DataStage assets..."            \
    mcix datastage import                           \
      --url "$CPD_URL"                              \
      --user "$CPD_USER"                            \
      --api-key "$CPD_APIKEY"                       \
      --project "My DataStage Project"              \
      --assets /workspace/project-overlayed         \
                                                    \
    echo "Compiling DataStage assets..."            \
    mcix datastage compile                          \
      --url "$CPD_URL"                              \
      --user "$CPD_USER"                            \
      --api-key "$CPD_APIKEY"                       \
      --project "My DataStage Project"              \
      --assets /workspace/project-overlayed         \
      --junit /workspace/results/compile-junit.xml
  '
```
