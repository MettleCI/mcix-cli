---
title: MCIX Command Line Interface
description: Modern software delivery for <br/>IBM DataStage NextGen
banner_src: ../../assets/img/banner.jpeg
---

<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/card-group.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/content-block-mixed.min.js"></script>
<script type="module" src="https://1.www.s81c.com/common/carbon-for-ibm-dotcom/version/v2.8.0/link-list.min.js"></script>

<c4d-link-list type="default" slot="complementary">
  <c4d-link-list-heading>Resources</c4d-link-list-heading>
  <c4d-link-list-item
    href="https://github.com/mettleci/mcix-cli/releases"
    target="mcix-releases"
    cta-type="local"
  >
    MCIX Releases
  </c4d-link-list-item>
  <c4d-link-list-item
    href="http://nextgen.mettleci.io/"
    target="mcix-docs"
    cta-type="local"
  >
    MettleCI Documentation
  </c4d-link-list-item>

  <c4d-link-list-item
    href="https://github.com/mettleci/mcix"
    target="mcix-github"
    cta-type="external"
  >
    MCIX GitHub Actions
  </c4d-link-list-item>

  <c4d-link-list-item
    href="https://dev.azure.com/mettleci/mcix"
    target="mcix-azure"
    cta-type="external"
  >
    MCIX Azure DevOps Tasks
  </c4d-link-list-item>
</c4d-link-list>

## Welcome to MCIX

<cds-inline-notification
  kind="error"
  title="Warning"
  subtitle="The MCIX command is currently a Technical Preview which should not be used for production purposes. 
  Beware that its commmands, options, and behaviour can change or disappear at any time without warning.
  Release of the production-ready version is anticipated by the end of 2026 Q2."
  low-contrast
  id="overlay-notification">
</cds-inline-notification>

This documentation provides an introduction to the MCIX Command Line Interface for IBM DataStage NextGen.  It is compatible with DataStage NextGen running on both self-hosted and Software-as-a-Service instances. 

The MCIX CLI tool is available for **Unix (x86)**, **Windows (x86)**, and **macOS (ARM64)**. The information presented on this site represents the latest version of the tool which can be downloaded  [here](https://github.com/mettleci/mcix-cli/releases/latest){:target="_blank" rel="noopener"}. 

## Start here

{% assign intro_pages = site.pages | where: "type", "introduction" | sort: "order" %}
<c4d-card-group>
  {% for page in intro_pages %}
    <c4d-card-group-item cta-type="local" href="{{ site.baseurl }}{{ page.url }}">
      <c4d-card-heading>{{ page.title }}</c4d-card-heading>
      <p>{{ page.description | strip_html | truncatewords: 10 }}</p>
      <c4d-card-footer></c4d-card-footer>
    </c4d-card-group-item>
  {% endfor %}
</c4d-card-group>

## Command reference

{% assign namespace_pages = site.pages | where: "type", "namespace" %}
<c4d-card-group>
  {% for page in namespace_pages %}
    <c4d-card-group-item cta-type="local" href="{{ site.baseurl }}{{ page.url }}">
      <c4d-card-heading>{{ page.title }}</c4d-card-heading>
      <p>{{ page.description | strip_html | truncatewords: 10 }}</p>
      <c4d-card-footer></c4d-card-footer>
    </c4d-card-group-item>
  {% endfor %}
</c4d-card-group>