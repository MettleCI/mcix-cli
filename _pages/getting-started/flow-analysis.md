---
status: draft #Status can be draft, reviewed or published.
owner: John McKeever
tags:
  - DataStage
  - Flow Analysis
---
# Introduction

Static code analysis is the analysis of a computer program's code without executing that code; In DataStage NextGen this is referred to as **Flow Analysis**.  This approach contrasts with dynamic program analysis, which is performed on programs during their execution and is achieved in DataStage by creating and running a DataStage [Unit Test Case](../testing/testing-datastage-flows.md).  

DataStage's flow analysis functionality validates one or more DataStage assets against a set of quality criteria defined in **Flow Analysis Rules**.  MettleCI ships with a set of [sample flow analysis rules](flow_rules.md) which provide a basis for customers to develop their own suite of flow analysis rules by either using the shipped rules as supplied, ignoring them, modifying them, or augmenting them with new customer-specific rules as required to meet specific needs.  

Flow analysis rules have a variety of applications:

- Enforcing coding standards in DataStage flows, improving the consistency, maintainabiity, and security of your solution
- Identifying external assets, which may require external management
- Identifying deprecated stages, allowing upgrade effort to be quantified.

Flow analysis rules are grouped into tags


Flow anlysis rules are also executable as part 
The Sort stage (highlighted) does not comply with an existing Compliance Rule designed to ensure naming standards.  Note that the DataStage custom menu actions shown in this page are installed by following the DataStage Integration Setup instructions.