"""
This module contains the APIClient class
which provides methods to send HTTP requests (GET, POST, DELETE)
to the specified base URL with specific headers.
"""
import requests

class APIClient:
    # This is a constructor of the class
    def __init__(self, base_url):
        self.base_url = base_url
        self.default_headers = {"x-api-key": "reqres-free-v1"}

    def get(self, endpoint, **kwargs):
        # Search and removes key word 'headers' from kwargs, and returns it value.
        # Otherwise, it will be a duplicate in the 'requests.get'
        headers = kwargs.pop("headers", {})
        combined_headers = {**self.default_headers, **headers}
        return requests.get(f"{self.base_url}{endpoint}", headers=combined_headers, **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        headers = kwargs.pop("headers", {})
        combined_headers = {**self.default_headers, **headers}
        return requests.post(f"{self.base_url}{endpoint}", data=data, json=json, headers=combined_headers, **kwargs)

    def delete(self, endpoint, **kwargs):
        headers = kwargs.pop("headers", {})
        combined_headers = {**self.default_headers, **headers}
        return requests.delete(f"{self.base_url}{endpoint}", headers=combined_headers, **kwargs)