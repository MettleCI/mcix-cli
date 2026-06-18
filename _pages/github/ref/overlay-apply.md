## overlay apply

This command applies changes - defined in a [json5-formatted](https://json5.org/){:target="_blank" rel="noopener"} overlay file - to one or more specified DataStage assets supplied in a directory or `.zip` file.

#### Parameters

| Name            | Required | Default  | Description |
| :-------        | :------- | :------- | :-------    |
| **assets**     | Yes      | -        | Path to DataStage export zip file or directory |
| **output**     | Yes      | -        | Zip file or directory to write updated assets |
| **overlay**    | Yes      | -        | Directory containing asset overlays. Each overlay will be applied in specified order when providing multiple (e.g., `-overlay dir1 -overlay dir2`)
| **properties** | -        | -        | Properties file with replacement values |

<details markdown="1">
  <summary>Example</summary>
```yaml
{% raw %}# mcix overlay apply
- name: mcix overlay apply
  uses: mettleci/mcix/overlay/apply@latest
  id: mcix-overlay-apply
  with:
    assets:     '${{ github.workspace }}/datastage'
    overlays:    ${{ github.workspace }}/overlays/common, ${{ github.workspace }}/overlays/${{ vars.ENVID }}
    properties: '${{ github.workspace }}/varfiles/var.${{ vars.ENVID }}'
    output:     '${{ github.workspace }}/build/release.zip'
{% endraw %}```
Where ...
- `vars.ENVID` is an environment identifier, such as 'CI'.
</details>

---
