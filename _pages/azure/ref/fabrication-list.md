## fabrication list

This command lists all the MettleCI data fabrication generators available in either…

- a supplied test data fabrication bundle file (or directory of bundle files), or
- the built-in MettleCI data fabrication generators

#### Parameters

| Name                  | Required | Default  | Description |
| :-------              | :------- | :------- | :-------    |
| **include-internal**  | Yes<br/>*(when path not specified)*              | - | Use pre-existing generators from MettleCI's internal libraries |
| **path**              | Yes<br/>*(when include-internal not specified)*  | - | The path to either a folder full of generators or a single `<generator>.json` file |
| **include-params**  | -        | -        |  Display parameters for each generator |

<details markdown="1">
  <summary>Examples</summary>

This example shows how to list the data fabrication generators in a supplied user-created `.json` bundle file - in this case, we'll list the capabilities of custom 'Star Wars' generator ...

```shell
{% raw %}# mettleci fabrication list
$> mettleci fabrication list \
   -path star_wars.json
{% endraw %}```

... which produces:

```shell
{% raw %}MettleCI Command Line (build 221)
(C) 2018-2022 Data Migrators Pty Ltd
fabrication list (v1.0-SNAPSHOT)
star_wars.call_sign
    Description: Generates a random Star Wars call sign, e.g. 'Red 5', 'Blue Leader'
star_wars.character
    Description: Generates a random Star Wars character name
star_wars.droid
    Description: Generates a random Star Wars droid name
star_wars.planet
    Description: Generates a random Star Wars planet name
star_wars.quote
    Description: Generates a random quote from a Star Wars character
star_wars.species
    Description: Generates a random Star Wars species name
star_wars.vehicle
    Description: Generates a random Star Wars vehicle name
star_wars.wookiee_word
    Description: Generates a random Wookiee word
{% endraw %}```

This example does the same but shows generator parameters ...

```shell
{% raw %}# mettleci fabrication list
$> mettleci fabrication list \
   -path star_wars.json -include-params
{% endraw %}```

... which produces:

```shell
{% raw %}MettleCI Command Line (build 221)
(C) 2018-2022 Data Migrators Pty Ltd
fabrication list (v1.0-SNAPSHOT)
star_wars.call_sign
    Description: Generates a random Star Wars call sign, e.g. 'Red 5', 'Blue Leader'
star_wars.character
    Description: Generates a random Star Wars character name
star_wars.droid
    Description: Generates a random Star Wars droid name
star_wars.planet
    Description: Generates a random Star Wars planet name
star_wars.quote
    Description: Generates a random quote from a Star Wars character
    Parameters:
    - character             STRING    (Nullable)
star_wars.species
    Description: Generates a random Star Wars species name
star_wars.vehicle
    Description: Generates a random Star Wars vehicle name
star_wars.wookiee_word
    Description: Generates a random Wookiee word
$>
{% endraw %}```
</details>
