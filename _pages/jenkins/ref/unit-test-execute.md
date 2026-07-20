## unit-test execute

[<img src="https://img.shields.io/badge/github-marketplace-blue?style=flat-square&logo=github">](https://github.com/marketplace/actions/mcix-unit-test-execute){:target="_blank" rel="noopener"} 

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

<details markdown="1">
  <summary>The 'report' option</summary>

The `reports` option is used to specify the directory into which the [JUnit](/introduction/junit-output) XML files produced by this command will be placed.  Each job tested will produce a separate XML file named after the Job (e.g. Job `MY_JOB_ABC` will produce a JUnit file named `MY_JOB_ABC.xml`)
</details>

<details markdown="1">
  <summary>The 'ignore-test-failures' option</summary>

The `ignore-test-failures` option will prevent a failing Unit Test from being interpreted as a command failure by your build system, and consequently halting your CI/CD pipeline. 

When using the `mcix unit-test execute` command to execute unit tests from within a build orchestration system (Jenkins, GitHub, Bamboo, GitLab, etc.) it’s important to understand how the command and your build system interact.  Calling the `mcix unit-test execute` command has three potential outcomes:

* The command executes **successfully** and runs a unit test which **passes**,
* The command executes **successfully** and runs a unit test which **fails**, or
* The command **fails to execute** and the unit test is never invoked. e.g., due to a misconfigured parameter such as referencing a non-existent unit test.

Like all shell commands, the `mcix unit-test execute` command returns an [exit code](https://en.wikipedia.org/wiki/Exit_status){:target="_blank" rel="noopener"} informing the host system of the success, or otherwise, of the invoked process - in this case a DataStage test case. By default, the `mcix unit-test execute` command returns a non-zero (failure) result when either the command cannot complete or **when a unit test fails**. For many build orchestration systems this will cause the build to fail instantly and, most importantly, prevent the publication of the failed test’s associated [JUnit XML file](https://junit.org){:target="_blank" rel="noopener"}, making the process of diagnosing the test failure difficult.

The `mcix unit-test execute -ignore-test-failures` option will prevent a failing unit test from being interpreted as a command failure by your build system, and consequently halting your CI/CD pipeline.
</details>

<details markdown="1">
  <summary>Example</summary>
```shell
{% raw %}# mcix unit-test execute
mcix unit-test execute \
  -url    '${env.CP4DHOSTNAME}" \
  -user    '${env.CP4DUSERNAME}" \
  -api-key "${apikey}" \
  -project "${env.DATASTAGE_PROJECT}" \
  -report "reports/unit-test-junit.xml" \
  -test-suite "MettleCI NextGen Unit Tests" \
  -include-asset-in-test-name
{% endraw %}```
</details>

---
