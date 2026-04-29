---
title: MettleCI MCIX Command Line Interface
---

<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/card-group.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block-mixed.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/link-list.min.js"></script>

<c4d-link-list type="default" slot="complementary">
  <c4d-link-list-heading>Resources</c4d-link-list-heading>
  <c4d-link-list-item
    href="https://docs.mettleci.com/"
    cta-type="local"
  >
    MettleCI Documentation
  </c4d-link-list-item>
  <c4d-link-list-item
    href="https://github.com/mettleci/mcix"
    cta-type="external"
  >
    MCIX GitHub Actions
  </c4d-link-list-item>
</c4d-link-list>

## Get started

Start by seeing the [repository releases](https://github.com/mettleci/mcix-cli/releases) for the latest version of the MettleCI MCIX Command Line Interface.

## Pages

Browse the topics covered in this documentation.

<c4d-card-group>
  {% for page in site.pages %}
    <c4d-card-group-item cta-type="local" href="{{ site.baseurl }}{{ page.url }}">
      <c4d-card-heading>{{ page.title }}</c4d-card-heading>
      <p>{{ page.excerpt | strip_html | truncatewords: 10 }}</p>
      <c4d-card-footer> </c4d-card-footer>
    </c4d-card-group-item>
  {% endfor %}
</c4d-card-group>
