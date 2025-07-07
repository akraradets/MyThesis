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

## FastAPI Module

This project now includes a FastAPI module for creating web APIs. The module is located in `src/fastapi_module/` and provides:

- RESTful API endpoints
- Interactive API documentation (Swagger UI)
- Integration with existing project modules (`mylib` and `mysecondlib`)
- Health check endpoints

### Running the FastAPI Server

To start the FastAPI server, run:

```sh
$ python run_api_server.py
```

The server will start at `http://localhost:8000` and you can access:

- **API Documentation**: `http://localhost:8000/docs` (Swagger UI)
- **Alternative API docs**: `http://localhost:8000/redoc` (ReDoc)
- **Health Check**: `http://localhost:8000/health`
- **API Endpoints**: `http://localhost:8000/api/`

### Available API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/greet/{name}` - Greet using MyObj
- `GET /api/greet2/{name}` - Greet using MyObjTwo  
- `GET /api/info` - Get API information

### Using the FastAPI Module

You can also import and use the FastAPI module in your code:

```python
from fastapi_module import app, router

# The app is a FastAPI instance that you can run or extend
# The router contains all the custom API routes
```