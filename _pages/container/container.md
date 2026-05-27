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
 Azure     | mettleci.azurecr.io/mettleci/mcix |
| GitHub    | ghcr.io/mettleci/mcix:latest |
| IBM       | icr.io/mettleci/mcix |
| DockerHub | docker pull mettleci/mcix:1.0.556 |

Retrieve the MCIX container image using the `docker pull` command then use [`docker run`](https://docs.docker.com/reference/cli/docker/container/run/) to invoke MCIX commands within a container instance of the image. 

<cds-inline-notification
  kind="info"
  title="Note"
  subtitle="If required, you can pull the MCIX container image from its public location and host it in your own private container registry."
  low-contrast
  id="overlay-notification">
</cds-inline-notification>

## Simplest example

Here's a basic example of calling `mcix datastage import` incide the MCIX container using `docker run`. 
The `--rm` flag in the docker run command instructs Docker to automatically remove the container and its file system once it exits.

```
docker run --rm \
  ghcr.io/mettleci/mcix:latest \
  mcix datastage export \
    -url "https://cpd.example.com" \
    -user "my-user" \
    -api-key "my-api-key" \
    -project "My DataStage Project" \
    -assets "/export"
```

## Mount a local filesystem


You can use the `-v` flag to mount a local directory in the container, so that files created by your MCIX commands remain available on the host once your container instance exits.  This example also uses the `-e` flag to set environment variables inside the running container:

```
docker run --rm \
  -v "$PWD/export:/export" \
  -e CPD_URL="https://cpd.example.com" \
  -e CPD_USER="my-user" \
  -e CPD_APIKEY="my-api-key" \
  ghcr.io/mettleci/mcix:latest \
  mcix datastage export \
    -url "$CPD_URL" \
    -user "$CPD_USER" \
    -api-key "$CPD_APIKEY" \
    -project "My DataStage Project" \
    -assets "/tmp/export"
```

## Invoke multiple commands

You can run multiple commands within a single instance of the container by passing your commands as a shell script parameter to the `-c` parameter.

This example mopunts multiple host directories into 

```
docker run --rm \
  --entrypoint /bin/sh \
  -v "$PWD/project:/workspace/project" \
  -v "$PWD/overlays:/workspace/overlays" \
  -v "$PWD/results:/workspace/results" \
  -e CPD_URL="https://cpd.example.com" \
  -e CPD_USER="my-user" \
  -e CPD_APIKEY="my-api-key" \
  ghcr.io/mettleci/mcix:latest \
  -c '
    set -e

    echo "Applying overlay..."
    mcix overlay apply \
      --source /workspace/project \
      --overlay /workspace/overlays/dev \
      --target /workspace/project-overlayed

    echo "Importing DataStage assets..."
    mcix datastage import \
      --url "$CPD_URL" \
      --user "$CPD_USER" \
      --api-key "$CPD_APIKEY" \
      --project "My DataStage Project" \
      --assets /workspace/project-overlayed

    echo "Compiling DataStage assets..."
    mcix datastage compile \
      --url "$CPD_URL" \
      --user "$CPD_USER" \
      --api-key "$CPD_APIKEY" \
      --project "My DataStage Project" \
      --assets /workspace/project-overlayed \
      --junit /workspace/results/datastage-compile-junit.xml
  '
```




```
# Create the output directory
mkdir -p ./mcix-results
```

Next, run the `mcix asset-analysis test` command with the `-junit` parameter directing output to the `asset-analysis-junit.xml` to the container's `/mcix-results` directory.

The important point

test results in the 

```
docker run --rm \
  -v "$PWD/mcix-results:/mcix-results" \
  ghcr.io/mettleci/mcix:latest \
  mcix asset-analysis test \
    --rules "/path/in/container/rules" \
    --project "/path/in/container/project" \
    --junit "/mcix-results/asset-analysis-junit.xml"

ls -l ./mcix-results
```

You should see something like:

asset-analysis-junit.xml

The important part is the volume mount:

```
-v "$PWD/mcix-results:/mcix-results"
```

That maps a local directory `./mcix-results` to the `/mcix-results` directory inside the container.


So when MCIX writes `/mcix-results/asset-analysis-junit.xml` the file is actually persisted on your host at `./mcix-results/asset-analysis-junit.xml`.

An improved approach could involve mounting both the source/project files and the output directory:

```
mkdir -p ./mcix-results

docker run --rm \
  -v "$PWD/project:/workspace/project" \
  -v "$PWD/rules:/workspace/rules" \
  -v "$PWD/mcix-results:/mcix-results" \
  ghcr.io/mettleci/mcix:latest \
  mcix asset-analysis test \
    --project "/workspace/project" \
    --rules "/workspace/rules" \
    --junit "/mcix-results/asset-analysis-junit.xml"

```