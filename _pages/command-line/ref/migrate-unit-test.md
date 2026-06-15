## migrate unit-test

![migrate unit-test syntax](img/migrate-unit-test.svg "migrate unit-test syntax")

Migrates a MettleCI unit testfrom DataStage Classic format to DataStage NextGen format .

#### Parameters

| Name           | Required | Default  | Description |
| :-------       | :------- | :------- | :-------    |
| **export**     | Yes      | -        | Target project export |
| **specs**      | Yes      | -        | Path to unit test specs directory to be used as the source of the migration |

<details markdown="1">
  <summary>Examples</summary>
```shell
{% raw %}# mcix migrate unit-test
MettleCI Command Line (build 1.0-SNAPSHOT)
(C) 2018-2026 Data Migrators Pty Ltd
Usage: datastage migrate-unit-test [options]
  Options:
  * -export
      Target project export
  * -specs
      Path to unit test specs directory to be used as the source of the
      migration
{% endraw %}```
</details>




















