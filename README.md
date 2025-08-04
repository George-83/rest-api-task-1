# Endava REST API Testing Project

This project provides automated tests for the public API [https://reqres.in](https://reqres.in), built using **Python**, **Pytest**, and the **Requests** library.

<pre>## 📁 Project Structure

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