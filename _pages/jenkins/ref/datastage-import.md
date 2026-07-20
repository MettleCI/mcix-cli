## datastage import

Imports DataStage assets from a DataStage export zip file or directory into a CP4D/CP4DaaS project.  This command produces a [JUnit-compatible](/introduxtion/junit-output) test output XML file which reports each individual job’s import status.


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
{% raw %}# mcix datastage import
mcix datastage import \
  -api-key $CP4DKEY \
  -url     $CP4DHOSTNAME \
  -user    $CP4DUSERNAME \
  -assets  dstage1.zip \
  -project dstage1 
{% endraw %}```
</details>

<details markdown="1">
  <summary>GitHub Action</summary>
```yaml
{% raw %}# mcix datastage import
- name: DataStage import using mcix datastage import action
  uses: mettleci/mcix/datastage/import@latest
  id: mcix-datastage-import
  with:
    api-key: ${{ secrets.CP4DKEY }}
    url:     ${{ vars.CP4DHOSTNAME }}
    user:    ${{ vars.CP4DUSERNAME }}
    project: ${{ env.DatastageProject }}
    assets:  '${{ github.workspace }}/datastage'
{% endraw %}```
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
{% raw %}# mcix datastage import 
mcixDatastageImport(
	url: "${env.CP4DHOSTNAME}",
	user: "${env.CP4DUSERNAME}",
	apiKeyCredentialsId: "CPDAPIKEYCRED",
    project: "${env.DATASTAGE_PROJECT}",
    assets: "datastage",
    report: "reports/import-junit.xml"
)
{% endraw %}```
</details>
