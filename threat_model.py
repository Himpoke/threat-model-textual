"""Application providing functionality for OTM files"""
from textual.app import App, ComposeResult
from textual.widgets import Header, Static, TabbedContent, TabPane
from schema_fetcher import read_otm
import json
import jsonschema

class ThreatModel(App):
    """Textual threat model app."""
    CSS_PATH = "threat_model.tcss"
    def compose(self) -> ComposeResult:
        """Compose our UI."""
        yield Header()
        self.title = "Open Threat Model Editor"

        with TabbedContent(initial="project"):
            with TabPane("Project", id="project"):
                yield Static("M: id, name")
                yield Static("id, name, description, owner, ownerContact, tags, attributes")
                yield Static("")
                yield Static("Represenations: list")
                yield Static("id, name, description, type, size, repository")
                yield Static("repository: url")
            with TabPane("Assets", id="assets"):
                yield Static("id, name, description, risk")
                yield Static("risk: confidentiality, integrity, availability, comment")
            with TabPane("Trust Zones", id="trustZones"):
                yield Static("id, name, type, description, risk, parent, representation, attributes")
            with TabPane("Components", id="components"):
                yield Static("id, name, description, type, parent, representations, assets, threats, tags, attributes")
            with TabPane("DataFlows", id="dataflows"):
                yield Static("id, name, description, bidirectional, source, destination, assets, threats, tags, attributes")

def read_example():
    with open("example.json",'r') as file:
        content = file.read()
        return json.loads(content)

def validate_input(json_data, json_schema):
    try:
        jsonschema.validate(instance=json_data, schema=json_schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False

if __name__ == "__main__":
    ThreatModel().run()
    schema = read_otm()
    print(str(schema))
    example = read_example()
    if not validate_input(example,schema):
        print("oh no")
    else:
        print(example)
