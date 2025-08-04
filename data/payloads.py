"""
This module contains payloads.
Generates unique 'first_name', 'last_name' and 'email' for request 'create user'.
"""
import uuid

def generate_unique_user_payload():
    return {
        "email": f"morpheus_{uuid.uuid4().hex[:6]}@zion.com",
        "first_name": f"Morpheus_{uuid.uuid4().hex[:6]}",
        "last_name": f"Leader_{uuid.uuid4().hex[:6]}"
    }