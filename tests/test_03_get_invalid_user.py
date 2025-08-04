"""
Tests for the third scenario - 'Try to get details of user that doesn't exist'
API endpoint: GET /api/users/{fake_user_id}

Includes:
- Validation of response status code (404)
- Validation of the empty response body
"""
class TestGetInvalidUser:

    def test_invalid_user_response_code_404(self, response_invalid_user):
        assert response_invalid_user.status_code == 404

    def test_empty_response(self, response_invalid_user):
        body = response_invalid_user.json()
        assert body == {}