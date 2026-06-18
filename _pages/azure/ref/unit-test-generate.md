## unit-test generate

Generates a DataStage test case for one or more specified DataStage flows.


#### Parameters

| Name         | Required | Default  | Description |
| :-------     | :------- | :------- | :-------    |
| **specs**    | Yes      | -        | ... |
| **assets**   | Yes      | -        | ... |
| **joblist**  | -        | -        | ... |
| **check-row-count-only** | - | -   | Causes the generation of a test case which checks row counts, rather than the default comparison of data row-by-row |

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
