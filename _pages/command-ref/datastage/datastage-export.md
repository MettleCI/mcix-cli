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
{% raw %}# mcix datastage export
mcix datastage export \
  -api-key     $CP4DKEY \
  -url         $CP4DHOSTNAME \
  -user        $CP4DUSERNAME \
  -export-path dstage1.zip \
  -project     dstage1 
{% endraw %}```
</details>

<details markdown="1">
  <summary>GitHub Action</summary>
```yaml
{% raw %}# mcix datastage export
- name: DataStage export using mcix datastage export action
  uses: mettleci/mcix/datastage/export@latest
  id: mcix-datastage-export
  with:
    api-key: ${{ secrets.CP4DKEY }}
    url:     ${{ vars.CP4DHOSTNAME }} 
    user:    ${{ vars.CP4DUSERNAME }} 
    project: ${{ env.DatastageProject }}
    assets: '${{ github.workspace }}/datastage'
{% endraw %}```
</details>

<details markdown="1">
  <summary>Azure DevOps Tasks</summary>
```yaml
{% raw %}# mcix datastage export
- task: mcixDatastageExport@1
  displayName: 'Export DataStage Assets'
  inputs:
    url:        ${{ parameters.CP4DHostName }}
    user:       ${{ parameters.CP4DUsername }}
    apiKey:     ${{ parameters.CP4DKey }}
    project:    ${{ parameters.DatastageProject }}
    exportPath: '$(Build.SourcesDirectory)/datastage'
    imageName:  'mettleci.azurecr.io/mettleci/mcix'
{% endraw %}```
</details>

<details markdown="1">
  <summary>Jenkins</summary>
```yaml
{% raw %}# mcix datastage export
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
{% endraw %}```
</details>
