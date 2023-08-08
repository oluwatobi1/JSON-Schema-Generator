
import os

from schema_parser import read_json, analyze_attributes, dump_schema

def main():
    """
    Main entry point of the JSON schema generation program.
    Reads JSON files, analyzes attributes, and generates schema files.
    """
    
    input_dir = '../data/'
    output_dir = '../schema/'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(input_dir, filename)
            data = read_json(file_path)
            # print("data")
            # print("data", data)
            attributes = data.get('message', {})
            # print("Attributes")
            print("Attributes",attributes.keys())
            schema = analyze_attributes(attributes)
            # print("schema::::")
            # print("schema::::", schema)
            dump_schema(schema, output_dir, f"{filename.split('.')[0]}_schema.json")

if __name__ == "__main__":
    main()
