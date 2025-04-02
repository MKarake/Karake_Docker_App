from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath("."))

from app import app


client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the CRUD API!"}
