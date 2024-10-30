import json
import jsonschema
import os
from threatmodel import ThreatModel, SchemaFetcher

def read_example():
    """Read example.json file"""
    with open(os.path.join(os.getcwd(),"example.json"), "r", encoding="utf-8") as file:
        file_content = file.read()
        print(file_content)
        return json.loads(file_content)


def validate_input(json_data, json_schema):
    """Validate input JSON data against jsonschema"""
    try:
        jsonschema.validate(instance=json_data, schema=json_schema)
        return True
    except jsonschema.ValidationError:
        return False


if __name__ == "__main__":
    """main method: read input and start app"""
    schema_fetcher = SchemaFetcher()
    schema = schema_fetcher.read_otm()
    example = read_example()
    if not validate_input(example, schema):
        exit(-1)
    app = ThreatModel(example)
    app.run()
