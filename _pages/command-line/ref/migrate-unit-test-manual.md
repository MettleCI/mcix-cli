## migrate unit-test-manual
![migrate unit-test syntax](img/migrate-unit-test-manual.svg "migrate unit-test syntax")

Migrates a MettleCI unit test from DataStage Classic format to DataStage NextGen format .

#### Parameters

| Name           | Required | Default  | Description |
| :-------       | :------- | :------- | :-------    |
| **api-key**       | Yes      | -        | CP4D/CP4DaaS API key |
| **url**           | Yes | - | Base url of CP4D/CP4DaaS |
| **user**          | Yes | - | CP4D/CP4DaaS username |
| **project**       | Yes<br/>*(when `project-id` not specified)* | - | Name of target project |
| **project-id**    | Yes<br/>*(when `project` not specified)*    | - | Id of target project |
| **export-path**   | Yes    | - | Path to DataStage export zip file or directory |
| **specs-path**    | Yes      | -        | Path to unit test specs directory to be used as the source of the migration |

<details markdown="1">
  <summary>Example</summary>
```shell
{% raw %}# mcix migrate unit-test-manual
MettleCI Command Line (build 1.0-SNAPSHOT)
(C) 2018-2026 Data Migrators Pty Ltd
Usage: datastage migrate-unit-test-manual [options]
  Options:
  * -api-key
      CP4D/CP4DaaS API key
  * -export
      Target project export
    -project
      Name of target project (required when -project-id not specified)
    -project-id
      Id of target project (required when -project not specified)
  * -specs
      Path to unit test specs directory to be used as the source of the
      migration
  * -test-data-archive
      Target archive containing migrated test data files.
  * -url
      Base url of CP4D/CP4DaaS
  * -user
      CP4D/CP4DaaS username
{% endraw %}```
</details>
