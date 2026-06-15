## datastage import

![datastage import syntax](img/datastage-import.svg "datastage import syntax")

Imports DataStage assets from a DataStage export zip file or directory into a CP4D/CP4DaaS project.  This command produces a [JUnit-compatible](/pipelines/junit-output) test output XML file which reports each individual job’s import status.


#### Parameters

| Name              | Required | Default  | Description |
| :-------          | :------- | :------- | :-------    |
| **api-key**       | Yes      | -        | CP4D/CP4DaaS API key |
| **url**           | Yes      | -        | Base url of CP4D/CP4DaaS |
| **user**          | Yes      | -        | CP4D/CP4DaaS username |
| **assets**        | Yes      | -        | Path to DataStage export zip file or directory |
| **project**       | Yes<br/>*(when `project-id` not specified)* | - | Name of target project |
| **project-id**    | Yes<br/>*(when `project` not specified)* | - | Id of target project | 

<details markdown="1">
  <summary>Example</summary>
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
