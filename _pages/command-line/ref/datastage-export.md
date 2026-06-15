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


<details markdown="1">
  <summary>Supported asset types</summary>

- Build Stage
- CFF Schema
- Connection
- Custom Stage
- Data Definition
- Environment
- Flows
- Java Library
- Job
- Match Specification
- Message Handler
- Orchestration flow (pipeline)
- Parallel Function
- Parameter Set
- Schema Library
- Standardization Rule
- Subflow
- Test Case
- Wrapped Stage

</details>

<details markdown="1">
  <summary>Example</summary>
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
