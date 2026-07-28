---
title: MCIX for GitHub
description: IBM DataStage NextGen support for<br/>GitHub Actions
banner_src: ../../assets/img/banner.jpeg
---

<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/card-group.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block-mixed.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/link-list.min.js"></script>

## GitHub Actions

{% assign intro_pages = site.pages | where: "tech", "github" | sort: "order" %}
<c4d-card-group>
  {% for page in intro_pages %}
    <c4d-card-group-item cta-type="local" href="{{ site.baseurl }}{{ page.url }}">
      <c4d-card-heading>{{ page.title }}</c4d-card-heading>
      <p>{{ page.description | strip_html | truncatewords: 10 }}</p>
      <c4d-card-footer></c4d-card-footer>
    </c4d-card-group-item>
  {% endfor %}
</c4d-card-group>
