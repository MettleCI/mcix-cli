## fabrication test

This command invokes a specific test data fabrication generator, from either…

- a supplied test data fabrication bundle file (or directory of bundle files), or
- MettleCI’s built-in data fabrication generators.

#### Parameters

| Name                  | Required | Default  | Description |
| :-------              | :------- | :------- | :-------    |
| **P, -parameters**   | -        | -        | Generator parameters<br/>Syntax: `-Pkey=value` |
| **generator**        | Yes      | -        | The generator to test |  
| **rowcount**         | -        | 5        | Number of rows to generate |
| **path**             | -        | -        | The path to either a folder containing generators or a single `<generator>.json` file |  
| **include-internal** | -        | False    | Include pre-existing generators from our internal libraries |

<details markdown="1">
  <summary>Examples</summary>

This example shows how to list the tags of a directory of Asset Analysis rules in both tabulated and CSV formats:

```shell
{% raw %}# Command usage
$> mettleci fabrication test
MettleCI Command Line (build 221)
(C) 2018-2022 Data Migrators Pty Ltd
The following option is required: [-generator]
Usage: fabrication test [options]
  Options:
  * -generator
      the generator to test
    -include-internal
      include pre-existing generators from our internal libraries
      Default: false
    -P, -parameters
      generator parameters
      Syntax: -Pkey=value
      Default: {}
    -path
      the path to either a folder full of generators or a single <generator>.json file
    -rowcount
      number of rows to generate
      Default: 5
Command failed.
```
```shell
# A test with the no parameters specified (which defaults to providing a quote from any Star Wars character)
$> mettleci fabrication test \
      -path . \
      -generator star_wars.quote
MettleCI Command Line (build 221)
(C) 2018-2022 Data Migrators Pty Ltd
fabrication test (v1.0-SNAPSHOT)
I will start my operations here, and pull the rebels apart piece by piece.
Twice the pride, double the fall.
Show me again, grandfather, and I will finish what you started.
You will remove these restraints and leave this cell with the door open.
You're smarter than a tree, aren't you?
```
```shell
# A test with the nullable 'character' parameter specified as 'darth_vader'
$> mettleci fabrication test \
      -path . \
      -generator star_wars.quote \
      -Pcharacter="darth_vader"
MettleCI Command Line (build 221)
(C) 2018-2022 Data Migrators Pty Ltd
fabrication test (v1.0-SNAPSHOT)
I find your lack of faith disturbing.
I hope so for your sake, the Emperor is not as forgiving as I am
You are a member of the rebel alliance, and a traitor.
I hope so for your sake, the Emperor is not as forgiving as I am
Impressive. Most impressive. Obi-Wan has taught you well.
$>
{% endraw %}```
</details>
