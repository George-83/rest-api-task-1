"""
Tests for the first scenario - 'List available users' API endpoint:
GET /api/users?page=1

Includes:
- Validation of response status code (200)
- JSON schema validation of the response body
- Few JSON response assertions
- Extraction and sorting of user data
"""
import jsonschema
from utils.schema_loader import load_json_schema

class TestListUsers:

    def test_users_response_code_200(self, response_users):
        assert response_users.status_code == 200

    def test_json_schema_validate(self, response_users):
        schema = load_json_schema("page_1_users_schema.json")
        jsonschema.validate(response_users.json(), schema)

    def test_page_field_is_one(self, response_users):
        body = response_users.json()
        assert body.get("page") == 1

    def test_body_contains_6_users(self, response_users):
        body = response_users.json()
        users = len(body.get("data"))
        assert users == 6

    def test_first_user_name_is_george(self, response_users):
        body = response_users.json()
        users = body.get("data")
        assert users[0].get("first_name") == "George"

    def test_at_least_one_contains_name_emma(self, response_users):
        body = response_users.json()
        users = body.get("data")
        assert any(user.get("first_name") == "Emma" for user in users)

    def test_extract_single_user_details(self, response_users):
        body = response_users.json()
        users = body.get("data")
        first_user = users[0]
        user_id = first_user.get("id")
        user_email = first_user.get("email")
        assert user_id is not None
        assert user_email is not None
        print(f"\nUser ID: {user_id}\nUser Email: {user_email}")

    def test_sort_users_by_first_name(self, response_users):
        body = response_users.json()
        users = body.get("data")
        sorted_users = sorted(users, key=lambda u: u["first_name"])
        print("\nSorted users by first name:")
        for user in sorted_users:
            print(f"{user['first_name']} {user['last_name']} - {user['email']}")