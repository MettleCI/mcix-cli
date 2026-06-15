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
