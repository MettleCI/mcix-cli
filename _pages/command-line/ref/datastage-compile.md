## datastage compile

![datastage compile syntax](img/datastage-compile.svg "datastage compile syntax")

Compiles a DataStage Job, producing a [JUnit-compatible](/introduction/junit-output) test output XML file which reports each individual job’s compilation result.

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

<details markdown="1">
  <summary>Example</summary>
```shell
{% raw %}# mcix datastage compile
mcix datastage compile \
  -api-key $CP4DKEY \
  -url     $CP4DHOSTNAME \
  -user    $CP4DUSERNAME \
  -report  mettleci_compilation.xml \
  -project dstage1 \
  -include-asset-in-test-name
{% endraw %}```
</details>

---
