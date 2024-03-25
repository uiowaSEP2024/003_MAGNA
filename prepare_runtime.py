#!/usr/bin/env python3

import toml
from packaging import version


def main():
    # Load pyproject.toml
    pyproject = toml.load("pyproject.toml")
    # Extract the Python version specification
    python_version_spec = pyproject["tool"]["poetry"]["dependencies"]["python"]

    # Assume the version is specified with a caret (^), e.g., "^3.11.8"
    # This script extracts the version number and assumes the minor version is acceptable
    # For more complex version handling, consider using the `packaging` library more extensively
    base_version = python_version_spec.strip("^")
    # Heroku requires a specific version, so we choose the base version directly.
    # In a real-world scenario, you'd ensure this version is available on Heroku.

    # Write the determined version to runtime.txt
    with open("runtime.txt", "w") as runtime_file:
        runtime_file.write(f"python-{base_version}")


if __name__ == "__main__":
    main()
