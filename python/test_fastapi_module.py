#!/usr/bin/env python3
"""
Simple integration test for the FastAPI module.
This script tests the basic functionality of the FastAPI module.
"""

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from fastapi.testclient import TestClient
from fastapi_module import app

def test_fastapi_module():
    """Test the FastAPI module functionality."""
    print("Testing FastAPI module...")
    
    # Create a test client
    client = TestClient(app)
    
    # Test root endpoint
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to MyThesis API"}
    print("✓ Root endpoint test passed")
    
    # Test health check
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "MyThesis API"
    print("✓ Health check test passed")
    
    # Test greet endpoint
    response = client.get("/api/greet/TestUser")
    assert response.status_code == 200
    data = response.json()
    assert data["greeting"] == "Hello, TestUser!"
    assert data["name"] == "TestUser"
    print("✓ Greet endpoint test passed")
    
    # Test greet2 endpoint
    response = client.get("/api/greet2/TestUser2")
    assert response.status_code == 200
    data = response.json()
    assert data["greeting"] == "Hello, TestUser2!"
    assert data["name"] == "TestUser2"
    print("✓ Greet2 endpoint test passed")
    
    # Test info endpoint
    response = client.get("/api/info")
    assert response.status_code == 200
    data = response.json()
    assert data["project"] == "MyThesis"
    assert "description" in data
    assert "features" in data
    print("✓ Info endpoint test passed")
    
    print("\nAll tests passed! ✓")

if __name__ == "__main__":
    # Install httpx if not available (required for TestClient)
    try:
        import httpx
    except ImportError:
        print("Installing httpx for testing...")
        os.system("pip install httpx --user")
    
    test_fastapi_module()