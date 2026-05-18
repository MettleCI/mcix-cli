---
status: reviewed
owner: John McKeever
tags:
  - DataStage
  - Creating Tests
---
# Testing flows with rejects

Most DataStage jobs can be tested via MettleCI’s Unit Testing function simply by replacing input and output stages. However, some job designs - while commonplace - will necessitate a more advanced Unit Testing configuration.  The sections below outline MettleCI Unit Test Spec patterns that best match these job designs.

???+ info "This patterns is handled automatically for you by DataStage"

    For DataStage flows that use this pattern the DataStage test case creation process will generate an appropriately structured test case specification. This page acts as a reference to explain the structure of the generated JSON test specification.

## Input stage with rejects

The Input stage can be Unit Tested by including both read and reject links in the given clause of the Unit Test Spec.

The CSV data specified for the rejects link should contain records that will actually test the flow of records through the reject path(s) of the job.

### Flow design

![representation of a DataStage flow using a reject](./images/ds-test-case-rejects1.png "test cases with rejects")

### Test specification

```json
{
   "given": [
      {
         "stage": "Input",
         "link": "Read" 
         "path": "Input-Read.csv",
      },
      {
         "stage": "Input",
         "link": "Rejects" 
         "path": "Input-Rejects.csv",
      }
   ],
   "when": {
      "parameters": { }
   },
   "then": [
   ]
}
```

### Result

![representation of a DataStage flow using a reject](./images/ds-test-case-rejects2.png "test cases with rejects")

## Output stage with rejects

The output stage can be Unit Tested by including:

* the write link in the then clause of the Unit Test Spec; and
* the reject in the given clause of the Unit Test Spec.

The CSV data specified for the rejects link should contain records that will actually test the flow of records through the reject path(s) of the job.

### Flow design

![representation of a DataStage flow](./images/ds-test-case-rejects3.png "stored procedure")


### Test specification

```json
{
   "given": [
      {
         "stage": "Output",
         "link": "Rejects",
         "path": "Output-Rejects.csv"
      }
   ],
   "when": {
      "parameters": { }
   },
   "then": [
      {
         "stage": "Output",
         "link": "Write",
         "path": "Output-Write.csv"
      }
   ]
}
```

### Result

![representation of a DataStage flow](./images/ds-test-case-rejects4.png "stored procedure")
