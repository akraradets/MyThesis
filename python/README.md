# Python package

This is the Python packge for development.
The intended usage is to use it with `.devcontainer`.

## Usage

This package use `uv` as a project manager.

The first time you spawn/clone this project, you should run `uv sync` to sync the dependencies.
Check your explorer that you have these folders created:
- .venv: this is where your pip packages are installed.
- .python: this is where your python interpreter is linked to.

## Basic UV

To add dependencies, you can use the `uv add` command.
```sh
$ uv add <package_name>
```

To remove dependencies, you can use the `uv remove` command.
```sh
$ uv remove <package_name>
```

To list available python version.
```sh
$ uv python list
```

To change/pin python version. This will create/change a `.python-version` file in the root of the project.
```sh
$ uv python pin <python_version>
```
*Note*: when you pin a python version, it will also update the `requires-python` in `pyproject.toml` file.
*Note*: everytime you change the python version, you should run `uv sync` to reinstall the appropriate dependencies.