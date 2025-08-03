"""
Tests for the 'List available users' API endpoint:
GET /api/users?page=1

Includes:
- Validation of response status code (200)
- JSON schema validation of the response body
- Few JSON response assertions
- Extraction and sorting of user data
"""
import jsonschema
import pytest
from utils.api_client import APIClient
from utils.schema_loader import load_json_schema

@pytest.fixture
def api_client(base_url):
    return APIClient(base_url)

class TestListUsers:

    def test_users_response_code_200(self, api_client):
        response = api_client.get("/api/users?page=1")
        assert response.status_code == 200

    def test_json_schema_validate(self, api_client):
        schema = load_json_schema("page_1_users_schema.json")
        response = api_client.get("/api/users?page=1")
        jsonschema.validate(response.json(), schema)