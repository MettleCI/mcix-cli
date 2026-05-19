---
title: DataStage Namespace
description: Providing interaction with IBM DataStage NextGen
status: reviewed #Status can be draft, reviewed or published. 
owner: John McKeever
type: namespace
tags:
  - CLI
  - Pipelines
  - DataStage
---
# datastage namespace

The datastage namespace contains commands for working with IBM Cloud Pak for Data (CP4D) DataStage assets.

---
## datastage compile

![datastage compile syntax](img/datastage-compile.svg "datastage compile syntax")

Compiles a DataStage Job, producing a [JUnit-compatible](../command-shell/junit-output) test output XML file which reports each individual job’s compilation result.

#### Parameters

| Name           | Required | Default  | Description |
| :-------       | :------- | :------- | :-------    |
| **api-key**    | Yes      | -        | CP4D/CP4DaaS API key |
| **url**        | Yes      | -        | Base url of CP4D/CP4DaaS |
| **user**       | Yes      | -        | CP4D/CP4DaaS username |
| **report**     | Yes      | -        | JUnit compilation report file |
| **project**    | Yes <br/>*(when `project-id` not specified)* | - | Name of target project |
| **project-id** | Yes <br/>*(when `project` not specified)* | - | Id of target project |
| **include-job-in-test-name** | - | False | Test case names will include the compiled asset name in the JUnit reports |

#### Examples 

<details markdown="1">
  <summary>Command Line</summary>
```shell
{% raw %}// mcix datastage compile
mcix datastage compile \
  -api-key $CP4DKEY \
  -url     $CP4DHOSTNAME \
  -user    $CP4DUSERNAME \
  -report  mettleci_compilation.xml \
  -project dstage1 \
  -include-asset-in-test-name
{% endraw %}```
</details>

<details markdown="1">
  <summary>GitHub Actions</summary>
```yaml
{% raw %}# mcix datastage compile 
- name: DataStage Compile using mcix datastage compile action
  uses: mettleci/mcix/datastage/compile@latest
  id: mcix-datastage-compile
  with:
    api-key: ${{ secrets.CP4DKEY }}
    url:     ${{ vars.CP4DHOSTNAME }}
    user:    ${{ vars.CP4DUSERNAME }}
    project: ${{ env.DatastageProject }}
{% endraw %}```
</details>

<details markdown="1">
  <summary>Azure DevOps Tasks</summary>
```yaml
{% raw %}# mcix datastage compile 
- task: mcixDatastageCompile@1
  displayName: 'Compile DataStage Assets'
  inputs:
    imageName: 'your.registry.com/namespace/mcix'
    url:        ${{ parameters.CP4DHostName }}
    user:       ${{ parameters.CP4DUsername }}
    apiKey:     ${{ parameters.CP4DKey }}
    project:    ${{ parameters.DatastageProject }}
    report:    '$(Build.SourcesDirectory)/log/compile/compilation_results.xml'
    includeAssetInTestName: true
{% endraw %}```
</details>

<details markdown="1">
  <summary>Jenkins</summary>
```yaml
TBD
```
</details>

---

## datastage export

![datastage export syntax](img/datastage-export.svg "datastage export syntax")

Exports DataStage assets from a DataStage CP4D/CP4DaaS project to a destination zip file.

#### Parameters

| Name              | Required | Default  | Description |
| :-------          | :------- | :------- | :-------    |
| **api-key**       | Yes      | -        | CP4D/CP4DaaS API key |
| **url**           | Yes | - | Base url of CP4D/CP4DaaS |
| **user**          | Yes | - | CP4D/CP4DaaS username |
| **export-path**   | Yes    | - | Path to DataStage export zip file or directory |
| **project**       | Yes<br/>*(when `project-id` not specified)* | - | Name of target project |
| **project-id**    | Yes<br/>*(when `project` not specified)*    | - | Id of target project |
| **include-binaries** | -   | False | Whether to include executable binaries in the export |

#### Examples


<details markdown="1">
  <summary>Command Line</summary>
```shell
mcix datastage export \
  -api-key     $CP4DKEY \
  -url         $CP4DHOSTNAME \
  -user        $CP4DUSERNAME \
  -export-path dstage1.zip \
  -project     dstage1 
```
</details>

<details markdown="1">
  <summary>GitHub Action</summary>
```yaml
- name: DataStage export using mcix datastage export action
  uses: mettleci/mcix/datastage/export@latest
  id: mcix-datastage-export
  with:
    api-key: {% raw %}${{ secrets.CP4DKEY }}{% endraw %}
    url:     {% raw %}${{ vars.CP4DHOSTNAME }}{% endraw %}
    user:    {% raw %}${{ vars.CP4DUSERNAME }}{% endraw %}
    project: {% raw %}${{ env.DatastageProject }}{% endraw %}         
    assets: {% raw %}'${{ github.workspace }}/datastage'{% endraw %}
```
</details>

<details markdown="1">
  <summary>Azure DevOps Tasks</summary>
```yaml
- task: mcixDatastageExport@1
  displayName: 'Export DataStage Assets'
  inputs:
    url:        {% raw %}${{ parameters.CP4DHostName }}{% endraw %}
    user:       {% raw %}${{ parameters.CP4DUsername }}{% endraw %}
    apiKey:     {% raw %}${{ parameters.CP4DKey }}{% endraw %}
    project:    {% raw %}${{ parameters.DatastageProject }}{% endraw %}
    exportPath: '$(Build.SourcesDirectory)/datastage'
    imageName:  'mettleci.azurecr.io/mettleci/mcix'
```
</details>

<details markdown="1">
  <summary>Jenkins</summary>
```yaml
@Library('mcix-jenkins-lib') _

pipeline {
    stages {
        stage("Export") {
            agent {
                docker {
                    registryUrl 'https://ghcr.io'
                    registryCredentialsId 'GHCR'
                    image 'ghcr.io/mettleci/mcix:latest'
                    args "-u root --entrypoint=''"
                }
            }
            steps {
                mcixDatastageExport(
                    url: "${CPD_URL}",
                    user: "${CPD_USER}",
                    apiKeyCredentialsId: "${CPD_APIKEY_CRED}",
                    project: "${CPD_PROJECT}",
                    assets: "${EXPORT_PATH}"
                )
           }
        }
    }
}
```
</details>

---

## datastage import

![datastage import syntax](img/datastage-import.svg "datastage import syntax")

Imports DataStage assets from a DataStage export zip file or directory into a CP4D/CP4DaaS project.  This command produces a [JUnit-compatible](../command-shell/junit-output) test output XML file which reports each individual job’s import status.


#### Parameters

| Name              | Required | Default  | Description |
| :-------          | :------- | :------- | :-------    |
| **api-key**       | Yes      | -        | CP4D/CP4DaaS API key |
| **url**           | Yes      | -        | Base url of CP4D/CP4DaaS |
| **user**          | Yes      | -        | CP4D/CP4DaaS username |
| **assets**        | Yes      | -        | Path to DataStage export zip file or directory |
| **project**       | Yes<br/>*(when `project-id` not specified)* | - | Name of target project |
| **project-id**    | Yes<br/>*(when `project` not specified)* | - | Id of target project | 

#### Examples

<details markdown="1">
  <summary>Command Line</summary>
```shell
mcix datastage import \
  -api-key $CP4DKEY \
  -url     $CP4DHOSTNAME \
  -user    $CP4DUSERNAME \
  -assets  dstage1.zip \
  -project dstage1 
```
</details>

<details markdown="1">
  <summary>GitHub Action</summary>
```yaml
- name: DataStage import using mcix datastage import action
  uses: mettleci/mcix/datastage/import@latest
  id: mcix-datastage-import
  with:
    api-key: {% raw %}${{ secrets.CP4DKEY }}{% endraw %}
    url:     {% raw %}${{ vars.CP4DHOSTNAME }}{% endraw %}
    user:    {% raw %}${{ vars.CP4DUSERNAME }}{% endraw %}
    project: {% raw %}${{ env.DatastageProject }}{% endraw %}
    assets:  {% raw %}'${{ github.workspace }}/datastage'{% endraw %}
```
</details>

<details markdown="1">
  <summary>Azure DevOps Tasks</summary>
```yaml
{% raw %}# mcix datastage import 
- task: mcixDatastageImport@1
  displayName: 'Import DataStage Assets'
  inputs:
    url:        ${{ parameters.CP4DHostName }}
    user:       ${{ parameters.CP4DUsername }}
    apiKey:     ${{ parameters.CP4DKey }}
    project:    ${{ parameters.DatastageProject }}
    assetsPath: '$(Build.SourcesDirectory)/datastage'
    imageName:  'mettleci.azurecr.io/mettleci/mcix'
{% endraw %}```
</details>

<details markdown="1">
  <summary>Jenkins</summary>
```yaml
TBD
```
</details>