## datastage compile

[<img src="https://img.shields.io/badge/github-marketplace-blue?style=flat-square&logo=github">](https://github.com/marketplace/actions/mcix-datastage-compile){:target="_blank" rel="noopener"} 

This action compiles a DataStage flow, producing a [JUnit-compatible](/introduction/junit-output) XML output 
file which reports each individual flow's compilation result.

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
```yaml
{% raw %}# mcix datastage compile 
- name: DataStage Compile using mcix datastage compile action
  uses: mettleci/mcix/datastage/compile@latest
  id: mcix-datastage-compile
  with:
    api-key: ${{ secrets.CP4DKEY }}
    url:     ${{ vars.CP4DHOSTNAME }}
    user:    ${{ vars.CP4DUSERNAME }}
    project: ${{ env.DatastageProject }}
{% endraw %}```
</details>

---
