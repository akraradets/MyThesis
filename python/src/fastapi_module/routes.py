"""API routes for the FastAPI module."""

from fastapi import APIRouter
from mylib import MyObj
from mysecondlib import MyObjTwo

router = APIRouter()

@router.get("/api/greet/{name}")
async def greet_person(name: str):
    """Greet a person using MyObj."""
    obj = MyObj(name)
    return {"greeting": obj.greet(), "name": name}

@router.get("/api/greet2/{name}")
async def greet_person_two(name: str):
    """Greet a person using MyObjTwo."""
    obj = MyObjTwo(name)
    return {"greeting": obj.greet(), "name": name}

@router.get("/api/info")
async def get_info():
    """Get information about the API."""
    return {
        "project": "MyThesis",
        "description": "A FastAPI module for thesis work",
        "features": ["Greeting API", "Health checks", "Custom objects integration"]
    }