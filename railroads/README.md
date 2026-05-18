Python grammar railroad diagrams
================================

Requirements:
 - `cairo`, e.g. `brew install cairo`

Edit namespace definitions in the `namespace` folder.  Add new namespace files to the directory (if required) and they'll get picked up automatically by the build script.

To rebuild the PNG and SVG files in the `pngs` and `svgs` folders, run:

```console
$ python main.py
```

Remember to commit these changes once creeted locally:

```console
$ git add namespaces pngs svgs
$ git commit -m "Updated railroad diagrams"
$ git push origin main
```

Credits
-------

- `railroad.py` is adapted from https://github.com/tabatkins/railroad-diagrams.git

