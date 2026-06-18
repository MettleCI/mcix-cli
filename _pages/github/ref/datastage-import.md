## datastage import

[<img src="https://img.shields.io/badge/github-marketplace-blue?style=flat-square&logo=github">](https://github.com/marketplace/actions/mcix-datastage-import){:target="_blank" rel="noopener"} 

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

<details markdown="1">
  <summary>Example</summary>
```yaml
{% raw %}# mcix datastage import
- name: DataStage import using mcix datastage import action
  uses: mettleci/mcix/datastage/import@latest
  id: mcix-datastage-import
  with:
    api-key: ${{ secrets.CP4DKEY }}
    url:     ${{ vars.CP4DHOSTNAME }}
    user:    ${{ vars.CP4DUSERNAME }}
    project: ${{ env.DatastageProject }}
    assets:  '${{ github.workspace }}/datastage'
{% endraw %}```
</details>

---
