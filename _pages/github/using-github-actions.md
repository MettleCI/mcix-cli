---
title: Using MCIX with GitHub Actions
description: All MCIX GitHub Actions
type: none
tech: github
order: 1
---

Server
https://docs.github.com/en/enterprise-server@3.21/admin/managing-github-actions-for-your-enterprise

## Introduction

MCIX actions are compatible with GitHub Enterprise Cloud and GitHub Enterprise Server. The way you configure each of these to use `mettleci/mcix` actions is described below. 

## GitHub Enterprise Cloud (SaaS)

Enterprise Cloud runs on [github.com](https://github.com), so public actions normally work directly. However, your enterprise or organisation policy may restrict the use of third-party actions.

To resolve this, an enterprise administrator should navigate to:

**Enterprise settings** → **Policies → Actions**

Alternatively, an organisation owner can navigate to:

**Organisation settings** → **Actions** → **General**

They can either allow all public actions or select:

**Allow enterprise, and select non-enterprise, actions and reusable workflows**

Following this you can add the relevant repositories to the **allow-list**. For all actions under your organisation, you could use the following pattern:

```
mettleci/*
```

For tighter control you can explicitly specify each action (and version) to which you want to permit access:

```
mettleci/mcix-asset-analysis-test@v1,
mettleci/mcix-datastage-compile@v1,
mettleci/mcix-datastage-deploy@v1,
mettleci/mcix-datastage-import@v1,
mettleci/mcix-overlay-apply@v1,
mettleci/mcix-system-version@v1,
mettleci/mcix-unit-test-execute@v1
```

Wildcards (recommended) are more flexible and can also allow access to every existing (and future) version of each action:

```
mettleci/mcix-*@*
```

If your enterprise requires actions to be pinned to a full commit SHA your pipelines will need to include the full SHA in each action reference:

```
- uses: mettleci/mcix-datastage-compile@<full-40-character-SHA-here>
```

For more information see the [GitHub Actions organisation policy documentation](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization).

## GitHub Enterprise Server (Self-hosted)

A self-hosted GitHub Enterprise Server instance cannot use GitHub actions by default.

The recommended approach is for the site administrator to enable **GitHub Connect**:

- Configure GitHub Actions on the Enterprise Server instance.
- Enable **GitHub Connect**.
- Open **Enterprise settings** → **GitHub Connect**.
- **Enable Users** can utilize actions from GitHub in workflow runs.
- Add your actions to the enterprise Actions **allow-list** if public actions are restricted.

Both the Enterprise Server instance and its self-hosted runners need outbound access to GitHub. No inbound connection from GitHub is required. Once configured, the normal reference can be used:

```yaml
- uses: mettleci/mcix-datastage-compile@v1
```

GitHub documents this under enabling automatic access to [github.com](https://github.com) actions with GitHub Connect.

### Offline or restricted Enterprise Server installations

If GitHub Connect is unavailable, the enterprise administrator must mirror selected action repositories into their Enterprise Server using GitHub’s [actions-sync](https://github.com/actions/actions-sync) utility.

For example:

```yaml
./actions-sync sync \
  --cache-dir cache \
  --destination-token "$GHES_TOKEN" \
  --destination-url "https://github.example.com" \
  --repo-name \
    "mettleci/mcix-datastage-compile:approved-actions/mcix-datastage-compile"
```

The customer would then change the workflow reference:

```yaml
- uses: approved-actions/mcix-datastage-compile@v1
```

The mirrored action must be resynchronised when you publish new releases. See GitHub’s [manual action synchronisation instructions](https://docs.github.com/en/enterprise-server/admin/github-actions/managing-access-to-actions-from-githubcom/manually-syncing-actions-from-githubcom).

Read more about how to [Manage access to actions from github.com](https://docs.github.com/en/enterprise-server/admin/managing-github-actions-for-your-enterprise/managing-access-to-actions-from-githubcom).