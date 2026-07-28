---
title: Azure DevOps MCIX Task Reference 
description: MCIX tasks for your<br/>Azure DevOps Pipelines
type: none
tech: azure
order: 6
# banner_src: ../../assets/img/banner.jpeg
---

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

---

{% if site.compliance == "Y" %}

{% include_relative ref/asset-analysis-test.md %}

{% endif %}

{% include_relative ref/datastage-compile.md %}

{% include_relative ref/datastage-deploy.md %}

{% include_relative ref/datastage-import.md %}

{% include_relative ref/overlay-apply.md %}

{% include_relative ref/system-version.md %}

{% include_relative ref/unit-test-execute.md %}
