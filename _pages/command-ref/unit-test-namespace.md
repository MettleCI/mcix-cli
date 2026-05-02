---
status: reviewed #Status can be draft, reviewed or published. 
owner: John McKeever
tags:
  - DataStage
  - Running Tests
---
# unit-test namespace

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

#### Example

```shell
mcix unittest generate \
  -assets /opt/dm/mci/jobs \
  -joblist ./joblist.txt \
  -specs /opt/dm/mci/testspecs
```

**Note**:

This command is not available as a CI/CD native GitHib Actions or Azure DevOps task/plugin as there is no identified need for this functionality within the context of a CI/CD pipeline. If you require this functionality within your CI/CD pipeline then you can invoke the command line directly using a command line pipeline task.

---

## unit-test execute

![unittest test syntax](img/unit-test-execute.svg "unittest test syntax")

Run one or more MettleCI Unit Tests against one or more DataStage jobs.

#### Parameters

| Name                     | Required | Default  | Description |
| :-------                 | :------- | :------- | :-------    |
| **api-key**              | Yes      | -        | CP4D/CP4DaaS API key |
| **url**                  | Yes      | -        | Base url of CP4D/CP4DaaS |
| **user**                 | Yes      | -        | CP4D/CP4DaaS username |
| **project**              | Yes<br/>*(when `project-id` not specified)* | - | Name of target project (required when -project-id not specified) |
| **project-id**           | Yes<br/>*(when `project` not specified)*    | - | Id of target project | 
| **report**               | Yes      | -        | JUnit test report file |
| **max-concurrency**      | -        | 8        | Maximum number of concurrently executing test case jobs to run |
| **ignore-test-failures** | -        | False    | Returns zero when testing completes regardless of failures |
| **test-suite**           | -        | test     | The test suite name for this invocation of unit testing |

The `reports` option is used to specify the directory into which the JUnit XML files produced by this command will be placed.  Each job tested will produce a separate XML file named after the Job (e.g. Job `MY_JOB_ABC` will produce a JUnit file named `MY_JOB_ABC.xml`)

The `ignore-test-failures` option will prevent a failing Unit Test from being interpreted as a command failure by your build system, and consequently halting your CI/CD pipeline. 

See [Repeatable DataStage Project Deployments]() for more details on how the -project-cache parameter is used to implement incremental tests. For more information on using the `-project-cache` parameter see our detailed explanation.

### The 'ignore-test-failures' option

MettleCI unit tests can be executed in two ways: 

1. Manually, using the Cloud Pak interface, or
2. From the command line using the `mcix unit-test execute` command.

When using the MettleCI command line to execute unit tests from within a build orchestration system (Jenkins, GitHub Actions, Bamboo, etc.) it’s important to understand how the `mcix unit-test execute` command and your build system interact.

Calling the `mcix unit-test execute` command has three potential outcomes:

* The command executes successfully and runs a unit test which passes,
* The command executes successfully and runs a unit test which fails, or
* The command fails to execute for any reason, and the unit test is never invoked (e.g. due to a misconfigured parameter such as referencing a non-existent unit test)

Like all shell commands, the `mcix unit-test execute` command returns an [exit code](https://en.wikipedia.org/wiki/Exit_status) informing the host system of the success, or otherwise, of the invoked process - in this case a DataStage test case. By default, the `mcix unit-test execute` command returns a non-zero (failure) result when either the command cannot complete or **when a unit test fails**. For many build orchestration systems this will cause the build to fail instantly and, most importantly, prevent the publication of the failed test’s associated [JUnit XML file](https://junit.org), making the process of diagnosing the test failure difficult.

The `mcix unit-test execute -ignore-test-failures` option will prevent a failing unit test from being interpreted as a command failure by your build system, and consequently halting your CI/CD pipeline.


#### Examples

##### Command Line

```shell
mcix unit-test execute \
  -domain services.datamigrators.io:59445 \
  -server engine.datamigrators.io \
  -username isadmin \
  -password my_password \
  -project my_project \
  -specs unittest \
  -reports unittest_reports \
  -project-cache "/mettleci/cache/engine.datamigrators.io/my_project"
```

##### GitHub Actions

```yaml
- name: Invoke 'mcix unit-test execute' action
  uses: mettleci/mcix/unit-test/execute@latest
  id: mcix-unittest-execute
  with:
    url: "${{ vars.CP4DHOSTNAME }}" 
    api-key: ${{ secrets.CP4DKEY }}
    user: ${{ vars.CP4DUSERNAME }}
    project: ${{ env.DatastageProject }}
    max-concurrency: "2"
    test-suite: "MettleCI CP4D Unit Tests - ${{ env.DatastageProject }}"
    report: "${{ github.workspace }}/unittest-reports/${{ env.DatastageProject }}.xml"
    ignore-test-failures: true
```

##### Azure DevOps Task

```yaml
- task: mcixUnitTestExecute@1
  inputs:
    url: ${{ parameters.CP4DHostName }}
    user: ${{ parameters.CP4DUsername }}
    apiKey: ${{ parameters.CP4DKey }}
    project: ${{ parameters.DatastageProject }}
    report: '$(Build.SourcesDirectory)/unittest-reports/${{ parameters.DatastageProject }}.xml'
    testSuite: 'MettleCI CP4D Unit Tests - ${{ parameters.DatastageProject }}'
    ignoreTestFailures: true
    imageName: 'mettleci.azurecr.io/mettleci/mcix'
  displayName: 'Run Unit Tests'
```

---