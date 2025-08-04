import pytest
from utils.api_client import APIClient
from data.payloads import generate_unique_user_payload
import uuid

# Returns the base URL for the API. Used as the foundation for all API requests
@pytest.fixture
def base_url():
    return "https://reqres.in"


# Creates an instance of APIClient with the base URL. Allows sending HTTP requests to the API in tests
@pytest.fixture
def api_client(base_url):
    return APIClient(base_url)


# Performs a GET request to /api/users?page=1 endpoint. Returns the Response object for assertions in tests
@pytest.fixture
def response_users(api_client):
    return api_client.get("/api/users?page=1")


# Performs a GET request to /api/users/3 endpoint. Returns the Response object for assertions in tests
@pytest.fixture
def response_user_id(api_client):
    return api_client.get("/api/users/3")


# Performs a GET request to fake generated user id, /api/users/{fake_user_id} endpoint. Returns the Response object for assertions in tests
@pytest.fixture
def response_invalid_user(api_client):
    fake_user_id = uuid.uuid4().hex[:9]
    return api_client.get(f"/api/users/{fake_user_id}")


# Performs a POST request to /api/users endpoint, creates a new user. Returns the Response object and the payload for assertions in tests
@pytest.fixture
def response_create_user(api_client):
    payload = generate_unique_user_payload()
    response = api_client.post("/api/users", json=payload)
    return response, payload


# Performs a DELETE request to /api/users{USER_ID} endpoint
# Function first creates a unique new user, then takes it user_id
# Then performs DELETE user with that user_id. Returns the Response object for assertions in tests
@pytest.fixture
def response_delete_user(api_client):
    payload = generate_unique_user_payload()
    response_create = api_client.post("/api/users", json=payload)
    user_id = response_create.json().get("id")
    response_delete = api_client.delete(f"/api/users/{user_id}")
    return response_delete