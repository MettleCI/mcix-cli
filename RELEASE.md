# Release Process

This repo...

- Does not store binaries in Git.
- Does not build from source here.
- This repo only ...
   - receives externally built binaries
   - validates filenames/version
   - signs/checksums
   - publishes GitHub release assets
   - updates Homebrew

This repository does include 'source code' in the releases, but this is simply the source code for the 
GitHub Pages documentation. The inclusion of these 'source code' artefacts is performed automatically
(and unavoidably) by GitHub when creating a release.

Repository maintainers should create MCIX CLI releases like this...

```
External build process
         |
         ▼
   CLI BINARIES
         |
         ▼
    Manually Zip
         |
         ▼
        ZIP
         |
         ▼
 Create draft release
         |
         ▼
Run 'publish' workflow
         |
         ▼
  Validate release
         |
         ▼
Delete draft release
```

You'll run a workflow with `workflow_dispatch`, provide a version, and upload binaries as a zipped input 
artifact.

```
mcix-release-input-v1.2.3.zip
├─ mcix_darwin_arm64
├─ mcix_linux_amd64
├─ mcix_linux_arm64
└─ mcix_windows_amd64.exe
```

## 1. Prepare your input ZIP locally

To create a release, you need to gather the compiled binaries for all supported platforms and package 
them together. Here's an example of how to do this at the command line:

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

You can also use `gh release create <tag> <files>...` to create a release with attached files, if you want to use the command line.


## 3. Run the workflow to create the release

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

The GitHub Actions validates the inputs and performs the following actions:

- checks expected filenames
- checks executability / --version (of the Linux variant)
- generates checksums
- publishes GitHub Release

The workflow creates:

```text
Release: v1.2.3
Assets:
  mcix_darwin_arm64
  mcix_linux_amd64
  mcix_windows_amd64.exe
  checksums.txt
```

## 4. Delete the staging release

After confirming the final release, delete:

```text
staging-v1.2.3
```

That keeps the repo clean and leaves only the real `mcix` CLI binary release.



