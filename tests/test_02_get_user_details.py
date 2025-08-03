"""
Tests for the second scenario - 'Get extracted user details' API endpoint:
GET /api/users/3

Includes:
- Validation of response status code (200)
- JSON schema validation of the response body
- Few JSON response assertions
- Extraction and sorting of user data
"""
import jsonschema
from utils.schema_loader import load_json_schema

class TestGetUserDetails:

    def test_get_single_user_details(self, response_user_id):
        assert response_user_id.status_code == 200

    def test_json_schema_validate(self, response_user_id):
        schema = load_json_schema("user_3_schema.json")
        jsonschema.validate(response_user_id.json(), schema)

    def test_user_id_is_3(self, response_user_id):
        body = response_user_id.json()
        user = body.get("data")
        assert user.get("id") == 3

    def test_first_and_last_names_are_correct(self, response_user_id):
        body = response_user_id.json()
        user = body.get("data")
        assert user.get("first_name") == "Emma"
        assert user.get("last_name") == "Wong"

    def test_support_text_contains_caddy(self, response_user_id):
        body = response_user_id.json()
        support_text = body.get("support", {}).get("text")
        assert "Caddy" in support_text