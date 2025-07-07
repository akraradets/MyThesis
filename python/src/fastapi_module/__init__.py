"""FastAPI module for the thesis project."""

from .main import app
from .routes import router

__all__ = ["app", "router"]