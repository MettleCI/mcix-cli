---
title: CI Concepts
description: The generic concepts behind effective CI/CD for DataStage NextGen 
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


## Environments

A CI environment is the automated environment where your software is built, tested, checked, packaged, or published as part of Continuous Integration.

In practice, it usually means the machine or container that runs your pipeline when you push code or open a pull request.

For example, in GitHub Actions, Azure DevOps, Jenkins, GitLab CI, or Tekton, the CI environment might:

- Check out your source code
- Install dependencies
- Build the application
- Run unit tests
- Run security or quality checks
- Package the result
- Publish binaries, Docker images, documentation, or reports



Note that the environment names used by the example pipelines published alongside MCIX are:

| Name | Description |
| ---- | ----------- |
| CI   | Continuous Integration |
| QA   | Quality Assurance |
| PERF | Performance |
| PROD | Production |
