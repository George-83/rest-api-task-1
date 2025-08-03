import pytest
from utils.api_client import APIClient

# Returns the base URL for the API. Used as the foundation for all API requests.
@pytest.fixture
def base_url():
    return "https://reqres.in"


# Creates an instance of APIClient with the base URL. Allows sending HTTP requests to the API in tests
@pytest.fixture
def api_client(base_url):
    return APIClient(base_url)


# Performs a GET request to /api/users?page=1 endpoint. Returns the Response object for assertions in tests.
@pytest.fixture
def response_users(api_client):
    return api_client.get("/api/users?page=1")

# Performs a GET request to /api/users/3 endpoint. Returns the Response object for assertions in tests.
@pytest.fixture
def response_user_id(api_client):
    return api_client.get("/api/users/3")