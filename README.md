# Endava REST API Testing Project

This project provides automated tests for the public API [https://reqres.in](https://reqres.in), built using **Python**, **Pytest**, and the **Requests** library.

## 📁 Project Structure

<pre>
project_root/
├── data/
│ ├── json_schemas/         # JSON schema files for response validation
│ └── payloads.py           # Dynamic payload generators for requests
├── tests/                  # Test modules organized by endpoint/functionality
│ ├── test_01_list_users.py
│ ├── test_02_get_user_details.py
│ └── ...
├── utils/
│ ├── api_client.py         # Custom API client class for HTTP methods
│ └── schema_loader.py      # Helper to load and use JSON schemas
├── conftest.py             # Global fixtures used across tests
├── pytest.ini              # Pytest configuration (e.g., markers)
├── requirements.txt        # List of project dependencies
</pre>

## ⚙️ Requirements

- Python 3.13+
- [Requests](https://pypi.org/project/requests/)
- [Pytest](https://pypi.org/project/pytest/)
- [Jsonschema](https://pypi.org/project/jsonschema/)

To install all dependencies:

```pip install -r requirements.txt```

## 🚀 How to Run Tests
``` pytest -v```

## ✅ Features Covered
1. GET list of users from page 1:
    * Validate response status code
    * Validate response JSON schema
    * Few JSON response assertions
    * Extract single user details (Id, Email)
    * Sort users by first name and print
2. GET single user details:
    * Validate response status code
    * Validate response JSON schema
    * Few JSON response assertions
3. GET non-existent user:
    * Validate response status code
    * Validate empty response body
4. POST create new unique user:
    * Validate response status code
    * Validate response JSON schema
    * Few JSON response assertions
5. DELETE created user:
    * Validate response status code
    * Validate empty response body
6. Parameterize base URL:
    * Move all related code to conftest.py for centralized configuration

## 📝 Notes
* All fixtures are defined in conftest.py and shared across tests
* Randomized test data ensures uniqueness on POST requests
* JSON schema files live in data/json_schemas/
* Project is designed to be scalable and extendable

## 👤 Author
Created as part of an API testing task for Endava, using Python, Pytest, and Requests.