"""
Tests for the fourth scenario - 'Create UNIQUE new user'
API endpoint: POST /api/users

Includes:
- Validation of response status code (201)
- JSON schema validation of the response body
- Few JSON response assertions
"""
import jsonschema
from utils.schema_loader import load_json_schema
from data.payloads import generate_unique_user_payload

class TestCreateUniqueUser:

    def test_new_user_response_code_201(self, response_create_user):
        assert response_create_user.status_code == 201

    def test_new_user_json_schema(self, response_create_user):
        schema = load_json_schema("create_user_schema.json")
        jsonschema.validate(response_create_user.json(), schema)

    def test_new_user_correct_data(self, api_client):
        payload = generate_unique_user_payload()
        response = api_client.post("/api/users", json=payload)
        body = response.json()
        assert body["email"] == payload["email"]
        assert body["first_name"] == payload["first_name"]
        assert body["last_name"] == payload["last_name"]
        assert "createdAt" in body