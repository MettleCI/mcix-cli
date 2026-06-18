## unit-test generate

![unittest generate syntax](img/unit-test-generate.svg "unittest generate syntax")

Generates a DataStage test case for one or more specified DataStage flows.

The optional `-check-row-count-only` flag will cause the generation of a test case which checks row counts, rather than the default option which is to compare data row-by-row.

#### Parameters

| Name         | Required | Default  | Description |
| :-------     | :------- | :------- | :-------    |
| **specs**    | Yes      | -        | ... |
| **assets**   | Yes      | -        | ... |
| **joblist**  | -        | -        | ... |
| **check-row-count-only** | - | -   | ... |

<details markdown="1">
  <summary>Example</summary>
```shell
{% raw %}# mcix unit-test generate
mcix unittest generate \
  -assets  /opt/dm/mci/jobs \
  -joblist joblist.txt \
  -specs   /opt/dm/mci/testspecs
{% endraw %}```
</details>
