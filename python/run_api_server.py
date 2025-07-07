#!/usr/bin/env python3
"""
FastAPI Server Runner

This script starts the FastAPI server for the MyThesis project.
Run this script to start the web API server.
"""

import sys
import os
import uvicorn

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from fastapi_module import app

def main():
    """Run the FastAPI server."""
    print("Starting MyThesis FastAPI Server...")
    print("API Documentation will be available at: http://localhost:8000/docs")
    print("API Base URL: http://localhost:8000")
    print("Press Ctrl+C to stop the server")
    
    try:
        uvicorn.run(
            "fastapi_module:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()