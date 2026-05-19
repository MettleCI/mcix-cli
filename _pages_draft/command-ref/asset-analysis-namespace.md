---
title: Asset Analysis Namespace
description: Performing MettleCI Asset Analysis operations
status: reviewed #Status can be draft, reviewed or published. 
owner: John McKeever
type: namespace
tags:
  - Pipeline
  - CLI
  - Asset Analysis
  - Tags
---
# asset-analysis namespace

The `asset-analysis` namespace contains commands for running MettleCI Asset Analysis Rules and Asset Queries from the command line.
 
---

## asset-analysis query
 
**Note**: This command is for running MettleCI Asset *Queries*. If you're looking for the **Asset Analysis Rules** returned by DataStage flow analysis then see the [asset-analysis test](#asset-analysis-test) Command.

![asset-analysis query syntax](img/asset-analysis-query.svg "asset-analysis query syntax")

The command line implementation of the Asset Analysis Query functionality exposes the low-level mechanism to produce a report listing the results of the specified Asset Queries.

#### Parameters

| Name              | Required | Default  | Description |
| :-------          | :------- | :------- | :-------    |
| ***queries***     | Yes      | -        | Location of all the query files |
| ***assets***      | Yes      | -        | Location of all json assets to query |
| ***report***      | Yes      | -        | Report name (`.csv`) |
| ***exclude-tag*** | -        | -        | Tags of asset queries to exclude (case insensitive)<br/>*(repeatable)* |
| ***include-tag*** | -        | -        | Tags of asset queries to include (case insensitive), includes everything by default<br/>*(repeatable)* |
| ***threads***     | -        | 1        | Number of threads of execution |

#### Examples

This example demonstrates how run Asset Queries against one or more ISX files. 

```shell
mcix asset-analysis query \
  -assets ./Jobs \
  -queries ./Queries \
  -report compliance.csv \
```

**Note**: This command is not available as a CI/CD native GitHub Actions or Azure DevOps task/plugin as there is no identified need for this functionality within the context of a CI/CD pipeline. If you require this functionality within your CI/CD pipeline then you can invoke the command line directly using a command line pipeline task.

---

## asset-analysis test

**Note**: This command is for running MettleCI Asset Analysis *Rules*. If you're looking for the **Asset Queries** typically used in a MettleCI Report Card then please see the [asset-analysis query](#asset-analysis-query) Command.

![compliance test syntax](img/asset-analysis-test.svg "compliance test syntax")

The command line implementation of the Compliance Test functionality enables the production of a Compliance Results report of the specified assets against the specified set of MettleCI Compliance Rules.

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

These examples demonstrate the use of the `asset-analysis test` command to execute a set of Flow Analysis Rules against one or more exported ISX files. Note that the asset path specification in the export command uses the [same wildcard rules](https://www.ibm.com/docs/en/iis/11.7.0?topic=command-asset-paths) as the `istool` command. 

##### Command Line

```shell
mcix asset-analysis test \
  -rules compliance_rules \
  -assets datastage \
  -report compliance_report_warn.xml \
  -junit \
  -project-cache ./project-cache \
  -test-suite warnings \
  -ignore-test-failures \
  -include-job-in-test-name
```

##### GitHub Actions

```yaml
- name: DataStage static code analysis using mcix asset-analysis test action
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
```

##### Azure DevOps Task

```yaml
- task: mcixAssetanalysisTest@1
  displayName: 'Asset Analysis Test'
  inputs:
    url: ${{ parameters.CP4DHostName }}
    user: ${{ parameters.CP4DUsername }}
    apiKey: ${{ parameters.CP4DKey }}
    project: ${{ parameters.DatastageProject }}
    rules: '$(Build.SourcesDirectory)/${{ parameters.AssetAnalysisRepoName }}'
    report: '$(Build.SourcesDirectory)/analysis-reports/${{ variables.suiteName }}.xml'
    includeTags: ${{ parameters.IncludeTags }}
    excludeTags: ${{ parameters.ExcludeTags }}
    ignoreTestFailures: true
    includeAssetInTestName: true
    testSuite: ${{ parameters.AssetAnalysisSuite }}
    imageName: 'your.registry.com/namespace/mcix'
    displayName: 'Run Asset Analysis (${{ parameters.AssetAnalysisSuite }})'
```

---