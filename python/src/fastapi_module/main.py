"""Main FastAPI application."""

from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="MyThesis API",
    description="A FastAPI module for the thesis project",
    version="1.0.0"
)

# Include the router
app.include_router(router)

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to MyThesis API"}

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "MyThesis API"}