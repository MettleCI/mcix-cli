## asset-analysis test

![Released](https://img.shields.io/badge/status-release_pending-orange?logo=github) [<img src="https://img.shields.io/badge/github-repository-blue?style=flat-square&logo=github">](https://github.com/MettleCI/mcix-asset-analysis-test){:target="_blank" rel="noopener"}

The **MCIX asset analysis test** action provides an automated quality gate for DataStage assets.  It examines exported DataStage assets and checks them against a defined set of rules, identifying issues such as poor design patterns, missing standards, naming problems, or other project-specific quality concerns before those assets are promoted further through a CI/CD pipeline.

<cds-inline-notification
  kind="info"
  title="Note"
  low-contrast
  hide-close-button="true"
  id="overlay-notification">
    <div class="cds--inline-notification__subtitle">
    <p>This actio is for running MettleCI Asset Analysis <i>Rules</i>. If you're looking for the <b>asset analysis query</b> operation then please see the <a href="/command-line/command-reference#asset-analysis-query">asset-analysis query CLI command</a>. The <b>asset analysis query</b> operation is not available as a GitHub action.</p>
  </div>
</cds-inline-notification>

#### Parameters

| Name              | Required | Default  | Description |
| :-------          | :------- | :------- | :-------    |
| **api-key**       | -        | -        | CP4D API key |
| **exclude-tag**   | -        | -        | Tags (case insensitive) of compliance rules to exclude ([Read more](../asset-analysis-rule-tags)) |
| **ignore-test-failures** | - | False | Returns zero when testing completes regardless of failures |
| **include-job-in-test-name** | - | False | Test case names will include the job name in the jUnit report |
| **include-tag**   | -        | -        | Tags (case insensitive)of compliance rules to include, includes everything by default ([Read more](../asset-analysis-rule-tags)) |
| **path**          | -        | -        | Location of project export directory or zip file |
| **project**       | -        | -        | Project Name |
| **report**        | Yes      | -        | Report name (`.csv` or `.xml`) |
| **rules**         | Yes      | -        | Location of all the rule files |
| **test-suite**    | -        | -        | Name of test suite being run, only required if running this command multiple times for the same project |
| **url**           | -        | -        | Base URL for CP4D instance |
| **username**      | -        | -        | CP4D user name |

#### Examples

<details markdown="1">
  <summary>Example</summary>
This examples demonstrate the use of the `asset-analysis test` command to execute a set of Flow Analysis Rules against one or more exported ISX files. Note that the asset path specification in the export command uses the [same wildcard rules](https://www.ibm.com/docs/en/iis/11.7.0?topic=command-asset-paths) as the `istool` command. 

```yaml
{% raw %}- name: DataStage static code analysis using mcix asset-analysis test action
  uses: mettleci/mcix/asset-analysis/test@latest
  id: mcix-asset-analysis-test
  with:
    api-key: ${{ secrets.CP4DKEY }}
    url: "${{ vars.CP4DHOSTNAME }}" 
    username: ${{ vars.CP4DUSERNAME }}
    project: ${{ env.DatastageProject }}         
    report: "${{ github.workspace }}/analysis-reports/report_${{ inputs.AnalysisSuite }}.xml"
    rules: "${{ github.workspace }}/analysis-rules/rules"
    included-tags: ${{ inputs.IncludeTags }}
    excluded-tags: ${{ inputs.ExcludeTags }}
    ignore-test-failures: true
    test-suite: "${{ inputs.AnalysisSuite }}"
{% endraw %}```
</details>>

---