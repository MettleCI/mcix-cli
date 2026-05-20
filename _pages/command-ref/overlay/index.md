---
title: Overlay Namespace
description: Enabling the automated adaptation of assets to target environments
status: reviewed #Status can be draft, reviewed or published. 
owner: John McKeever
type: namespace
tags:
  - Pipeline
  - CLI
---
# Overlay Namespace

The `overlay` namespace contains commands wich enable you to define and apply changes to DataStage assets in order to modify their behavior or configuration without altering the original asset directly. This is particularly useful in scenarios where you want to maintain different configurations for different environments (e.g., development, testing, production) or when you want to apply temporary changes for specific use cases.

---

{% include_relative overlay-apply.md %}
