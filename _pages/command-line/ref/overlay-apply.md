## overlay apply

![overlay apply](img/overlay-apply.svg "overlay apply syntax")

**Note:** A detailed description of the role and use of overlays is provided [here](/introduction/overlays-introduction)

The `overlay` namespace contains commands wich enable you to define and apply changes to DataStage assets in order to modify their behavior or configuration without altering the original asset directly. This is particularly useful in scenarios where you want to maintain different configurations for different environments (e.g., development, testing, production) or when you want to apply temporary changes for specific use cases.

This command applies changes - defined in a [json5-formatted](https://json5.org/){:target="_blank" rel="noopener"} overlay file - to one or more specified DataStage assets supplied in a directory or `.zip` file.

#### Parameters

| Name            | Required | Default  | Description |
| :-------        | :------- | :------- | :-------    |
| **assets**     | Yes      | -        | Path to DataStage export zip file or directory |
| **output**     | Yes      | -        | Zip file or directory to write updated assets |
| **overlay**    | Yes      | -        | Directory containing asset overlays. Each overlay will be applied in specified order when providing multiple (e.g., `-overlay dir1 -overlay dir2`)
| **properties** | -        | -        | Properties file with replacement values |

<details markdown="1">
  <summary>Examples</summary>
```shell
{% raw %}# mcix overlay apply 
mcix overlay apply \
    -assets /path/to/datastage-export.zip \
    -output /path/to/updated-assets.zip \
    -overlay /path/to/overlay-directory \
    -properties /path/to/properties-file.properties
{% endraw %}```
</details>
