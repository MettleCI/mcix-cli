## datastage compile

Compiles a DataStage Job, producing a [JUnit-compatible](..//introduxtion/junit-output) test output XML file which reports each individual job’s compilation result.

#### Parameters

| Name           | Required | Default  | Description |
| :-------       | :------- | :------- | :-------    |
| **api-key**    | Yes      | -        | CP4D/CP4DaaS API key |
| **url**        | Yes      | -        | Base url of CP4D/CP4DaaS |
| **user**       | Yes      | -        | CP4D/CP4DaaS username |
| **report**     | Yes      | -        | JUnit compilation report file |
| **project**    | Yes <br/>*(when `project-id` not specified)* | - | Name of target project |
| **project-id** | Yes <br/>*(when `project` not specified)* | - | Id of target project |
| **include-job-in-test-name** | - | False | Test case names will include the compiled asset name in the JUnit reports |

#### Examples 

<details markdown="1">
  <summary>Command Line</summary>
```shell
{% raw %}# mcix datastage compile
mcix datastage compile \
  -api-key $CP4DKEY \
  -url     $CP4DHOSTNAME \
  -user    $CP4DUSERNAME \
  -report  mettleci_compilation.xml \
  -project dstage1 \
  -include-asset-in-test-name
{% endraw %}```
</details>

<details markdown="1">
  <summary>GitHub Actions</summary>
```yaml
{% raw %}# mcix datastage compile 
- name: DataStage Compile using mcix datastage compile action
  uses: mettleci/mcix/datastage/compile@latest
  id: mcix-datastage-compile
  with:
    api-key: ${{ secrets.CP4DKEY }}
    url:     ${{ vars.CP4DHOSTNAME }}
    user:    ${{ vars.CP4DUSERNAME }}
    project: ${{ env.DatastageProject }}
{% endraw %}```
</details>

<details markdown="1">
  <summary>Azure DevOps Tasks</summary>
```yaml
{% raw %}# mcix datastage compile 
- task: mcixDatastageCompile@1
  displayName: 'Compile DataStage Assets'
  inputs:
    imageName: 'your.registry.com/namespace/mcix'
    url:        ${{ parameters.CP4DHostName }}
    user:       ${{ parameters.CP4DUsername }}
    apiKey:     ${{ parameters.CP4DKey }}
    project:    ${{ parameters.DatastageProject }}
    report:    '$(Build.SourcesDirectory)/log/compile/compilation_results.xml'
    includeAssetInTestName: true
{% endraw %}```
</details>

<details markdown="1">
  <summary>Jenkins</summary>
```yaml
{% raw %}# mcix datastage compile 
@Library('mcix-jenkins-lib') _
pipeline {
    stages {
        stage("Export") {
            agent {
                docker {
                    registryUrl 'https://ghcr.io'
                    registryCredentialsId 'GHCR'
                    image 'ghcr.io/mettleci/mcix:latest'
                    args "-u root --entrypoint=''"
                }
            }
            steps {
                mcixDatastageCompile(
                    url: "${CPD_URL}",
                    user: "${CPD_USER}",
                    apiKeyCredentialsId: "${CPD_APIKEY_CRED}",
                    project: "${CPD_PROJECT}",
                    assets: "${EXPORT_PATH}"
                    includeAssetInTestName: true
                )
           }
        }
    }
}
{% endraw %}```
</details>
