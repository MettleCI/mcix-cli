## asset-analysis test

**Note**: This command is for running MettleCI Asset Analysis *Rules*. If you're looking for the **Asset Queries** typically used in a MettleCI Report Card then please see the [asset-analysis query](#asset-analysis-query) Command.

![compliance test syntax](img/asset-analysis-test.svg "compliance test syntax")

The **MCIX asset analysis test** command provides an automated quality gate for DataStage assets.  It examines exported DataStage assets and checks them against a defined set of rules, identifying issues such as poor design patterns, missing standards, naming problems, or other project-specific quality concerns before those assets are promoted further through a CI/CD pipeline.

#### Parameters

| Name              | Required | Default  | Description |
| :-------          | :------- | :------- | :-------    |
| **api-key**       | -        | -        | CP4D API key |
| **exclude-tag**   | -        | -        | Tags (case insensitive) of compliance rules to exclude |
| **ignore-test-failures** | - | False | Returns zero when testing completes regardless of failures |
| **include-job-in-test-name** | - | False | Test case names will include the job name in the jUnit report |
| **include-tag**   | -        | -        | Tags (case insensitive)of compliance rules to include, includes everything by default |
| **path**          | -        | -        | Location of project export directory or zip file |
| **project**       | -        | -        | Project Name |
| **report**        | Yes      | -        | Report name (`.csv` or `.xml`) |
| **rules**         | Yes      | -        | Location of all the rule files |
| **test-suite**    | -        | -        | Name of test suite being run, only required if running this command multiple times for the same project |
| **url**           | -        | -        | Base URL for CP4D instance |
| **username**      | -        | -        | CP4D user name |

<details markdown="1">
  <summary>Example</summary>
These examples demonstrate the use of the `asset-analysis test` command to execute a set of asset analysis rules against one or more exported asset files. Note that the asset path specification in the export command uses the [same wildcard rules](https://www.ibm.com/docs/en/iis/11.7.0?topic=command-asset-paths) as the `istool` command. 

```shell
mcix asset-analysis test \
  -rules compliance_rules \
  -assets datastage \
  -report compliance_report_warn.xml \
  -junit \
  -test-suite warnings \
  -ignore-test-failures \
  -include-job-in-test-name
```
</details>

---

