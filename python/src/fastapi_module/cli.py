"""CLI script to run the FastAPI server."""

import uvicorn
from fastapi_module import app

def main():
    """Run the FastAPI server."""
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()