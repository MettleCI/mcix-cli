## overlay apply

![overlay apply](img/overlay-apply.svg "overlay apply syntax")

This command applies changes - defined in a [json5-formatted](https://json5.org/){:target="_blank" rel="noopener"} overlay file - to one or more specified DataStage assets supplied in a directory or `.zip` file.

#### Parameters

| Name            | Required | Default  | Description |
| :-------        | :------- | :------- | :-------    |
| **assets**     | Yes      | -        | Path to DataStage export zip file or directory |
| **output**     | Yes      | -        | Zip file or directory to write updated assets |
| **overlay**    | Yes      | -        | Directory containing asset overlays. Each overlay will be applied in specified order when providing multiple (e.g., `-overlay dir1 -overlay dir2`)
| **properties** | -        | -        | Properties file with replacement values |

#### Examples

<details markdown="1">
  <summary>Command Line</summary>
```shell
{% raw %}# mcix overlay apply 
mcix overlay apply \
    -assets /path/to/datastage-export.zip \
    -output /path/to/updated-assets.zip \
    -overlay /path/to/overlay-directory \
    -properties /path/to/properties-file.properties
{% endraw %}```
</details>

<details markdown="1">
  <summary>GitHub Actions</summary>
```yaml
{% raw %}# mcix overlay apply
- name: mcix overlay apply
  uses: mettleci/mcix/overlay/apply@latest
  id: mcix-overlay-apply
  with:
    assets:     '${{ github.workspace }}/datastage'
    overlays:   ${{ github.workspace }}/overlays/common, ${{ github.workspace }}/overlays/${{ vars.ENVID }}
    properties: '${{ github.workspace }}/varfiles/var.${{ vars.ENVID }}'
    output: "${{ github.workspace }}/build/release.zip"
{% endraw %}```
Where ...
- `vars.ENVID` is an environment identifier, such as 'CI'.
</details>

<details markdown="1">
  <summary>Azure DevOps Task</summary>
```yaml
{% raw %}# mcix overlay apply
- task: mcixOverlayApply@1
  displayName: 'Apply Overlays to Assets'
  inputs:
      assets: 'datastage'
      overlays: |
      '$(Build.SourcesDirectory)/overlays/common'
      '$(Build.SourcesDirectory)/overlays/${{  }}'
      properties: '$(Build.SourcesDirectory)/varfiles/var.${{ parameters.EnvironmentID }}'
      output: '$(Build.SourcesDirectory)/release.zip'
      imageName: 'your.registry.com/namespace/mcix'
{% endraw %}```
Where ...
- `parameters.EnvironmentID` is an environment identifier, such as 'CI'.
</details>

<details markdown="1">
  <summary>Jenkins</summary>
```yaml
{% raw %}# mcix overlay apply 
stage("Deploy") {
    agent {
        docker {
            registryUrl 'https://ghcr.io'
            registryCredentialsId 'GHCR'
            image 'ghcr.io/mettleci/mcix:latest'
            args "-u root --entrypoint=''"
        }
    }
    steps {
        mcixOverlayApply(
            assets: "datastage",
            overlays: "overlays/common,overlays/${env.ENVID}",
            properties: "varfiles/var.${env.ENVID}",
            output: "build/release.zip"
        )
    }
  }
{% endraw %}```
Where ...
- `env.ENVID` is an environment identifier, such as 'CI'.
</details>
