"""
Tests for the fifth scenario - 'Delete newly created user'
API endpoint: DELETE /api/users{USER_ID}

Includes:
- Validation of response status code (204)
- Validation of the empty response body
"""
class TestDeleteUser:

    def test_delete_user_status_code_204(self, response_delete_user):
        assert response_delete_user.status_code == 204

    def test_delete_user_empty_response(self, response_delete_user):
        assert response_delete_user.text == ""