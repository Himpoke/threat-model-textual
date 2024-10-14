import requests
import os
import json

file_path = "otm_schema.json"
def fetch_otm():
    openThreatModelUrl = "https://raw.githubusercontent.com/iriusrisk/OpenThreatModel/refs/heads/main/otm_schema.json"
    response = requests.get(openThreatModelUrl)

    if response.status_code != 200:
        print("Error fetching otm model")
        exit(-1)

    threatModdelingJsonSchema = response.json()
    with open(file_path, 'w') as file:
        file.write(json.dumps(threatModdelingJsonSchema))
    return threatModdelingJsonSchema

def read_otm():
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.loads(file.read())
    else:
        return fetch_otm()
