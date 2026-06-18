## datastage compile

```yaml
{% raw %}
# mcix datastage compile 
- task: mcixDatastageCompile@1
  displayName: 'Compile DataStage Assets'
  inputs:
    imageName: 'your.registry.com/namespace/mcix'
    url:        CP4DHostName
    user:       CP4DUsername
    apiKey:     CP4DKey
    project:    DatastageProject
    report:    'log/compile/compilation_results.xml'
    includeAssetInTestName: true
{% endraw %}
```


Compiles a DataStage Job, producing a [JUnit-compatible](../../command-shell/junit-output) test output XML file which reports each individual job’s compilation result.

### Parameters

| Name           | Required | Default  | Description |
| :-------       | :------- | :------- | :-------    |
| **api-key**    | Yes      | -        | CP4D/CP4DaaS API key |
| **url**        | Yes      | -        | Base url of CP4D/CP4DaaS |
| **user**       | Yes      | -        | CP4D/CP4DaaS username |
| **report**     | Yes      | -        | JUnit compilation report file |
| **project**    | Yes <br/>*(when `project-id` not specified)* | - | Name of target project |
| **project-id** | Yes <br/>*(when `project` not specified)* | - | Id of target project |
| **include-job-in-test-name** | - | False | Test case names will include the compiled asset name in the JUnit reports |

<details markdown="1">
  <summary>Example</summary>
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
