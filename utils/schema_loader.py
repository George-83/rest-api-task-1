"""
This module provides utility function to load JSON schemas
from the 'data/json_schemas' directory for API response validation.
"""
import json
from pathlib import Path

def load_json_schema(filename):
    schema_path = Path(__file__).parent.parent / "data" / "json_schemas" / filename
    with open(schema_path, encoding="utf-8") as f:
        return json.load(f)