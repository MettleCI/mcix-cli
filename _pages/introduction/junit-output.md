---
title: Test results using JUnit
description: The de facto standard for<br/>reporting test results
# banner_src: ../../assets/img/banner.jpeg
---

## What is JUnit?

[JUnit](https://junit.org/){:target="_blank" rel="noopener"} is a unit testing framework which 
plays a crucial role test-driven development, and is part of a family of unit testing frameworks 
collectively known as xUnit. The JUnit XML output format is widely understood by build and test 
tools and is a good choice for tools wishing to describe their test outcomes. Here is a summary 
of a JUnit output file, showing a skipped, failed and passed result.

```XML
<?xml version="1.0" encoding="UTF-8"?>
<testsuites>
   <testsuite name="MyTestSuiteName" errors="0" tests="0" failures="0" time="0" timestamp="2000-01-01T11:12:13" />
   <testsuite name="MyOtherTestSuiteName" errors="0" skipped="1" tests="3" failures="1" time="0.006" timestamp="2000-01-02T11:12:13">
      <properties>
         <property name="MyName1" value="one" />
         <property name="MyName2" value="two" />
         <property name="MyName3" value="three" />
      </properties>
      <testcase classname="MyTest1" name="should default path to an empty string" time="0.006">
         <failure message="test failure">Assertion failed</failure>
      </testcase>
      <testcase classname="MyTest2" name="should default consolidate to true" time="0">
         <skipped />
      </testcase>
      <testcase classname="MyTest3" name="should default some other thing to true" time="0" />
   </testsuite>
</testsuites>
```

## Applications

Some build tools, such as Azure DevOps and Jenkins, have in-built support for parsing JUnit and presenting those results to users and tracking their change over time.  

Others, such as GitHub, have no understanding of JUnit and so it is often left to the user to capture the JUnit file and process them in some fashion. Fortunately, the MCIX [GitHub Custom Actions](../container/github) process the JUnit files for you and present their results as easily digestible GitHub Step Summaries.

## Schema

The JUnit XML output is produced by a number of MCIX commands and despite being widely adopted its spcification is somewhat loose. There have been a number of attempts to codify the schema, but here’s a working [XSD](https://en.wikipedia.org/wiki/XML_Schema_(W3C)){:target="_blank" rel="noopener"} for the JUnit format:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![JUnit XML Schema]({{ site.url }}/assets/img/document--download.svg)]({{ site.url }}/assets/files/junit.xml.zip)
<br/>[Download]({{ site.url }}/assets/files/junit.xml.zip)
