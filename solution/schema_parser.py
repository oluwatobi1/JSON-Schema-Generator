import os
import json


def read_json(file_path):
    """
    Read a JSON file and return its content as a Python dictionary.

    Parameters:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Parsed JSON content as a dictionary.
    """
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def analyze_attributes(data):
    """
    Analyze attributes within a JSON data dictionary and generate a schema representation.

    Parameters:
        data (dict): JSON data dictionary to analyze.

    Returns:
        dict: JSON schema representation of the analyzed attributes.
    """
    schema = {}
    payload = {
        "tag": "",
        "description": "",
        "required": False
    }

    for key, value in data.items():
        if isinstance(value, str):
            schema[key] = {
                **payload,
                "type": "string"
            }
        elif isinstance(value, int):
            schema[key] = { 
                **payload,
                "type": "integer"
            }
        elif isinstance(value, list):
            if all(isinstance(item, str) for item in value):
                schema[key] = { 
                    **payload,
                    "type": "enum"
                }
            elif all(isinstance(item, dict) for item in value):
                schema[key] = { 
                    **payload,
                    "type": "array"
                }
    return schema


def dump_schema(schema, output_dir, file_name):

    """
    Dump a JSON schema representation to a file.

    Parameters:
        output_dir (str): Directory path where the schema file will be saved.
        file_name (str): Name of the schema file to be saved.
    """

    output_path = os.path.join(output_dir, file_name)
    with open(output_path, 'w') as schema_file:
        json.dump(schema, schema_file, indent=4)
