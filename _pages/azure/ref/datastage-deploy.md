## datastage deploy

```yaml
{% raw %}
- task: mcixDatastageDeployt@1
  displayName: 'Import DataStage Assets'
  inputs:
    url:        CP4DHostName
    user:       CP4DUsername }}
    apiKey:     CP4DKey }}
    project:    DatastageProject
    assetsPath: /datastage'
    imageName:  'MyOrg.registry.io/MyOrg/mcix'
    blah:
    blah:
    blah:
    blah:
{% endraw %}
```

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
| **blah**          | -        | -        | Blah | 
| **blah**          | -        | -        | Blah | 
| **blah**          | -        | -        | Blah | 
| **blah**          | -        | -        | Blah | 

<details markdown="1">
  <summary>Example</summary>
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

---
