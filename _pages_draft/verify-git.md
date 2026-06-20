## Verify essential Git operations

From inside the cloned repository, run:

```bash
git pull
```

If this completes successfully (usually with an `Already up to date` message) you have permission to retrieve the latest repository content.  

Append a line to the `README.md` file:

```bash
echo "Git access check" >> README.md
```

<details markdown="1">
  <summary>Verify this step</summary>
Check the Git status to verify the change has been identified locally:

```
git status
```

This should show your change is not yet staged for commit:

```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")```
```
</details>

Stage it for commit:

```bash
git add README.md
```

<details markdown="1">
  <summary>Verify this step</summary>
Check the change has been staged for commit:

```
git status
```

This should show:

```
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   README.md
```
</details>


Now Commit it:

```
git commit -m "Updated README to verify Git access"
```

If the commit succeeds, your local Git configuration is working. 

Push the test change:

```bash
git push -u origin main
```

If this succeeds, you have the necessary write access to the repository.
-->