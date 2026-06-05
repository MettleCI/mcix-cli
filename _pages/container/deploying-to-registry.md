---
title: Specifying your container registry 
description: Deploying the MCIX container to your preferred registry 
# banner_src: ../../assets/img/banner.jpeg
---

<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/card-group.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block-mixed.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/link-list.min.js"></script>

<c4d-link-list type="default" slot="complementary">
  <c4d-link-list-heading>Resources</c4d-link-list-heading>
  <c4d-link-list-item
    href="https://marketplace.visualstudio.com/items?itemName=MettleCI.mcix"
    target="mcix-azure"
    cta-type="external"
  >
    MCIX for Azure DevOps on Visual Studio Marketplace
  </c4d-link-list-item>
</c4d-link-list>

# Copying the MCIX container image to your preferred registry

This guide shows how to copy the MCIX container image from one registry to another.  This can be useful for customers operating in highly-regulate environments which do not permit the pull of remotely-hopsted container images.  This page described how you can copy the MCIX image from the public registry on the IBM Container Registry:

```text
icr.io/mcix
```

... to another registry.  In this example we'll use Azure Container Registry:

```text
<registry-name>.azurecr.io
```

The process is:

1. Pull the image from the source registry.
2. Retag the image for the target registry.
3. Log in to the target registry.
4. Push the image to the target registry.

---

## Prerequisites

You need:

* Docker installed and running.
* Permission to pull the image from the source registry.
* Permission to push images to the target registry.
* The full source image name.
* The full target image name.

For example:

```text
Source image:
icr.io/mcix/mcix:1.2.3

Target image:
myregistry.azurecr.io/example-namespace/mcix:1.2.3
```

## 1. Pull the image from the source registry

Pull the image from the existing registry:

```bash
docker pull icr.io/example-namespace/mcix:1.2.3
```

This downloads the image to your local machine.

## 2. Tag the image for the target registry

Docker images are identified by their registry, repository name, and tag.
To prepare the image for the new registry, apply a new tag:

```bash
docker tag \
  icr.io/example-namespace/mcix:1.2.3 \
  myregistry.azurecr.io/example-namespace/mcix:1.2.3
```

This does not create a new image. It simply gives the existing image another name pointing to the target registry.

## 3. Log in to the target registry

For Azure Container Registry, log in using the Azure CLI:

```bash
az acr login --name myregistry
```

Alternatively, you can use Docker login directly:

```bash
docker login myregistry.azurecr.io
```

You must have permission to push images to the target registry.

## 4. Push the image to the target registry

Push the retagged image:

```bash
docker push myregistry.azurecr.io/example-namespace/mcix:1.2.3
```

Once complete, the image is available from the target registry.

## 5. Verify the image can be pulled

You can verify the image by pulling it back from the target registry:

```bash
docker pull myregistry.azurecr.io/example-namespace/mcix:1.2.3
```

You can also remove the local copy first to prove it is being retrieved from the target registry:

```bash
docker image rm myregistry.azurecr.io/example-namespace/mcix:1.2.3

docker pull myregistry.azurecr.io/example-namespace/mcix:1.2.3
```

## 6. Set container references

You'll need to ensure that the native actions/tasks used by your build system uses the correct reference to your newly-depoyed container.

#### Azure DevOps

#### GitHub

#### Jenkins

#### Other container-based systems


## Complete example

```bash
SOURCE_IMAGE="icr.io/example-namespace/mcix:1.2.3"
TARGET_IMAGE="myregistry.azurecr.io/example-namespace/mcix:1.2.3"

docker pull "$SOURCE_IMAGE"

docker tag "$SOURCE_IMAGE" "$TARGET_IMAGE"

az acr login --name myregistry

docker push "$TARGET_IMAGE"
```

---

## Notes

- The tag (e.g. `1.2.3) should usually be preserved when copying between registries.
- Avoid pushing everything as `latest` unless your organisation has a clear tagging policy. Versioned tags make deployments easier to audit and reproduce.

