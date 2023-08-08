
## JSON Schema Generator
This script reads JSON files, analyzes attributes within the "message" key, and generates a JSON schema based on specified rules. The generated schema is saved in the ./schema/ directory.

### Getting Started
1. Clone this repository to your local machine.

2. No additional installation required.

3. Place your JSON files in the ./data/ directory.

4. To generate the JSON schemas, run the script by executing the following command in your terminal:

`python3 main.py`

The generated schema files will be saved in the ./schema/ directory.

6. To run unit test  run the script by executing the following command in your terminal:

`python3 -m unittest`

### Additional Information
All attributes in the JSON schema are padded with "tag" and "description" keys.
The schema output captures ONLY the attributes within the "message" key of the input JSON source data.
>> Attributes within the key "attributes" are excluded.
>> All properties in the JSON schema are set to "required": false.
>> Data types in the JSON schema:
>> STRING: Identified as a string and mapped accordingly in the JSON schema output.
>> INTEGER: Identified as an integer and mapped accordingly in the JSON schema output.
>> ENUM: When a value in an array is a string, the program maps the data type as an ENUM.
>> ARRAY: When a value in an array is another JSON object, the program maps the data type as an ARRAY.
