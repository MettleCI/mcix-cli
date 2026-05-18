# Release Process

This repo...

Does not store binaries in Git.
Does not build from source here.
This repo only ...
  - receives externally built binaries
  - validates filenames/version
  - signs/checksums
  - publishes GitHub release assets
  - updates Homebrew

Repository maintainers should create MCIX CLI releases like this...

```
External build process
        │
        ▼
You provide binaries manually or via upload
        │
        ▼
GitHub Actions validates them
        │
        ├─ checks expected filenames
        ├─ checks executability / --version
        ├─ generates checksums
        ├─ signs assets
        ├─ creates attestations
        ├─ publishes GitHub Release
        └─ updates Homebrew tap
```

You'll run a workflow with `workflow_dispatch`, provide a version, and upload binaries as a zipped input artifact.

```
mcix-release-input-v1.2.3.zip
├─ mcix_darwin_arm64
├─ mcix_linux_amd64
├─ mcix_linux_arm64
└─ mcix_windows_amd64.exe
```



















Start by manually preparing one ZIP file containing the binaries, then trigger a GitHub Action that validates and publishes them as GitHub Release assets.

## 1. Prepare your input ZIP locally

Create this exact structure:

```text
mcix-release-input-v1.2.3.zip
├─ mcix_darwin_arm64
├─ mcix_linux_amd64
└─ mcix_windows_amd64.exe
```

Create it:

# Creating a release
To create a release, you need to gather the compiled binaries for all supported platforms and package them together. Here's an example of how to do this at the command line:

```bash
cd {path to local clone of this repository}

mkdir mcix-release-input-v1.2.3

cp /path/to/mcix-linux-x86.zip     mcix-release-input-v1.2.3/
cp /path/to/mcix-macos-arm64.zip   mcix-release-input-v1.2.3/
cp /path/to/mcix-windows-x86.zip   mcix-release-input-v1.2.3/

chmod +x mcix-release-input-v1.2.3/mcix_*

zip -r mcix-release-input-v1.2.3.zip mcix-release-input-v1.2.3
```

## 2. Create a draft GitHub Release as staging

Create a **draft release** manually in GitHub by clicking *Create a new release* under **Releases**:

```text
Tag:   staging-v1.2.3
Title: mcix release input v1.2.3
```

Upload:

```text
mcix-release-input-v1.2.3.zip
```

This draft release is just a staging place. The final release will be `v1.2.3`.

## 3. Add this workflow

Create:

```text
.github/workflows/publish-binary-release.yml
```

```yaml
name: Publish binary release

on:
  workflow_dispatch:
    inputs:
      version:
        description: "Version without leading v, e.g. 1.2.3"
        required: true
      staging_tag:
        description: "Draft/staging release tag containing input ZIP"
        required: true
        default: "staging-v1.2.3"
      input_zip:
        description: "Name of uploaded ZIP asset"
        required: true
        default: "mcix-release-input-v1.2.3.zip"

permissions:
  contents: write

jobs:
  publish:
    runs-on: ubuntu-latest
    environment: release

    steps:
      - name: Download staged input ZIP
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          set -euo pipefail

          mkdir -p incoming dist

          gh release download "${{ inputs.staging_tag }}" \
            --pattern "${{ inputs.input_zip }}" \
            --dir incoming

          unzip "incoming/${{ inputs.input_zip }}" -d incoming/unpacked

      - name: Locate unpacked binaries
        run: |
          set -euo pipefail

          ROOT="$(find incoming/unpacked -type f -name 'mcix_linux_amd64' -exec dirname {} \; | head -n 1)"

          if [ -z "$ROOT" ]; then
            echo "Could not locate unpacked mcix binaries"
            exit 1
          fi

          echo "BINARY_ROOT=$ROOT" >> "$GITHUB_ENV"

      - name: Validate supplied binaries
        run: |
          set -euo pipefail

          required=(
            mcix_darwin_arm64
            mcix_linux_amd64
            mcix_windows_amd64.exe
          )

          for file in "${required[@]}"; do
            if [ ! -f "$BINARY_ROOT/$file" ]; then
              echo "Missing required binary: $file"
              exit 1
            fi
          done

          cp "$BINARY_ROOT"/mcix_* dist/
          chmod +x dist/mcix_* || true

      - name: Smoke test Linux binary
        run: |
          set -euo pipefail

          ./dist/mcix_linux_amd64 --version || {
            echo "mcix_linux_amd64 --version failed"
            exit 1
          }

      - name: Generate checksums
        run: |
          set -euo pipefail

          cd dist
          sha256sum mcix_* > checksums.txt

      - name: Create final GitHub Release
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          set -euo pipefail

          TAG="v${{ inputs.version }}"

          gh release create "$TAG" \
            dist/* \
            --title "${{ inputs.version }}" \
            --notes "mcix ${{ inputs.version }}"
```

`gh release download` downloads assets from an existing GitHub Release, and `gh release create <tag> <files>...` creates a release with attached files. ([GitHub CLI][1])

## 4. Run the workflow

Go to:

```text
GitHub repo → Actions → Publish binary release → Run workflow
```

Use:

```text
version:     1.2.3
staging_tag: staging-v1.2.3
input_zip:   mcix-release-input-v1.2.3.zip
```

The workflow creates:

```text
Release: v1.2.3
Assets:
  mcix_darwin_arm64
  mcix_linux_amd64
  mcix_windows_amd64.exe
  checksums.txt
```

## 5. Delete the staging release

After confirming the final release, delete:

```text
staging-v1.2.3
```

That keeps the repo clean and leaves only the real `mcix` CLI binary release.
