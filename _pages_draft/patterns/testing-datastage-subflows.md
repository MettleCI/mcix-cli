---
status: reviewed
owner: John McKeever
tags:
  - DataStage
  - Creating Tests
---
# Testing flow with sub-flows

???+ info "This patterns is handled automatically for you by DataStage"

    For DataStage flows that use this pattern the DataStage test case creation process will generate an appropriately structured test case specification. This page acts as a reference to explain the structure of the generated JSON test specification.

Let's take a simple example of a DataStage test case:

![representation of a DataStage job showing CSV files being injected into source stages and an output stage referring to a CSV file which does not exist](./images/ds-test-case-simple2.png "test baseline screen capture")

Subflows, both local and components, complicate this situation as stage names in DataStage are only unique within a given flow or container.  

Consider writing a test specification for the following flow, `ProcessAccounts`, which includes a shared subflow stage `ContainerC1` which is itself a reference to the shared subflow `scWriteAccounts`:

Flow `ProcessAccounts`:
![representation of a DataStage flow using a shared container](./images/ds-test-case-container2.png "test cases using containers")

Container `scWriteAccounts`:
![representation of a DataStage shared container](./images/ds-test-case-container5.png "test cases using containers") |

You might be tempted to create a spec like this ...

```json
{
    "given": [
        {
            "path": "given.csv",
            "stage": "sfInput",
            "link": "in" 
        }
    ],
    "when": {},
    "then": [
        {
            "path": "expected.csv",
            "stage": "sfOutput",
            "link": "out"
        }
    ]
}
```

The resulting Unit Test Spec is ambiguous because the MettleCI Unit Test Harness will not be able to uniquely identify which Unit Test Data file is associated with each sqAccounts stage.  To avoid these sort of issues, the stage properties within Unit Test Specs expect fully qualified stage names.  A fully qualified stage name is prefixed with any relevant parent Container names using the format `<container name>.<stage name>`.

Here’s an example of a fully qualified stage name:

```json
{
    "given": [
        {
            "path": "given.csv",
            "stage": "sfInput",
            "link": "in" 
        }
    ],
    "when": {},
    "then": [
        {
            "path": "expected.csv",
            "stage": "subflow_1.sfOutput",
            "link": "out"
        }
    ]
}
```
