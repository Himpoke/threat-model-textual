import requests
import os
import json

class SchemaFetcher:
    def __init__(self):
        self.file_path = "otm_schema.json"
    
    def fetch_otm(self):
        openThreatModelUrl = "https://raw.githubusercontent.com/iriusrisk/OpenThreatModel/refs/heads/main/otm_schema.json"
        response = requests.get(openThreatModelUrl)

        if response.status_code != 200:
            print("Error fetching otm model")
            exit(-1)

        threatModdelingJsonSchema = response.json()
        with open(self.file_path, 'w') as file:
            file.write(json.dumps(threatModdelingJsonSchema))
        return threatModdelingJsonSchema

    def read_otm(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.loads(file.read())
        else:
            return self.fetch_otm()
