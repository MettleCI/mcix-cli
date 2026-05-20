import os
import cairosvg
import importlib
from railroad import *

# Folder containing all namespace_*.py files
NAMESPACE_DIR = "namespace"

# Collect statements from all namespace modules
statements = {}

def load_namespace_modules():
    for filename in os.listdir(NAMESPACE_DIR):
        if filename.startswith("namespace_") and filename.endswith(".py"):
            module_name = filename[:-3]  # strip .py
            module = importlib.import_module(f"{NAMESPACE_DIR}.{module_name}")
            # Merge any dicts named the same as module_name without the prefix
            # e.g. namespace_compliance.py contains a dict called "compliance"
            for name, value in vars(module).items():
                if not name.startswith("__"):  # ignore builtins
                    if isinstance(value, dict):
                        statements.update(value)

# Ensure output subdirectories exist
SVG_DIR = "svgs"
PNG_DIR = "pngs"
os.makedirs(SVG_DIR, exist_ok=True)
os.makedirs(PNG_DIR, exist_ok=True)

def main():
    load_namespace_modules()
    for key, value in statements.items():
        print ("Processing {0}".format(key))

        # Save SVG into svgs/
        svg_path = os.path.join(SVG_DIR, f"{key}.svg")
        with open(svg_path, "w") as out_svg:
            diagram = value
            diagram.writeSvg(out_svg.write)

        # Convert SVG → PNG into pngs/
        png_path = os.path.join(PNG_DIR, f"{key}.png")
        cairosvg.svg2png(
            url=svg_path,
            write_to=png_path,
            output_width=3000,
            dpi=300
        )

if __name__ == "__main__":
    main()
