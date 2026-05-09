import json
from typing import Any

def read_file(filepath: str) -> str:
    """
    Reads the entire content of a file given its filepath.
    Returns the content as a string.
    """
    with open(filepath, 'r') as file:
        return file.read()

def read_json(filepath: str) -> Any:
    """
    Reads and parses a JSON file.
    
    Example:
        data = read_json('data.json')
    """
    with open(filepath, 'r') as file:
        return json.load(file)
