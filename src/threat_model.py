"""Application providing functionality for OTM files"""

import json
import jsonschema
from textual.app import App, ComposeResult
from textual.widgets import Static, Header, TabbedContent, TabPane

try:
    from .classes import Project
    from .schema_fetcher import read_otm
except ImportError:
    from classes import Project
    from schema_fetcher import read_otm

content = {}


class ThreatModel(App):
    """Textual threat model app."""

    CSS_PATH = "threat_model.tcss"
    
    def __init__(self):
        super().__init__()
        self.title = "Open Threat Model Editor"
        self.tabbedcontent = None
        self.tab_project = None

    def compose(self) -> ComposeResult:
        """Compose our UI."""
        yield Header()
        self.tabbedcontent = TabbedContent(id="project_viewer", initial="project")

        with self.tabbedcontent:
            with TabPane("Project", id="project"):
                yield Project(id="project")
            with TabPane("Assets", id="assets"):
                yield Static("id, name, description, risk")
                yield Static("risk: confidentiality, integrity, availability, comment")
            with TabPane("Trust Zones", id="trustZones"):
                yield Static(
                    "id, name, type, description, risk, parent, representation, attributes"
                )
            with TabPane("Components", id="components"):
                yield Static(
                    "id, name, description, type, parent, representations, assets, threats, tags, attributes"
                )
            with TabPane("DataFlows", id="dataflows"):
                yield Static(
                    "id, name, description, bidirectional, source, destination, assets, threats, tags, attributes"
                )

    def on_mount(self):
        """ran after everything is rendered"""
        self.query_one("#project", Project).load_content(content["project"])


def read_example():
    """Read example.json file"""
    with open("example.json", "r", encoding="utf-8") as file:
        file_content = file.read()
        return json.loads(file_content)


def validate_input(json_data, json_schema):
    """Validate input JSON data against jsonschema"""
    try:
        jsonschema.validate(instance=json_data, schema=json_schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False


if __name__ == "__main__":
    schema = read_otm()
    example = read_example()
    if not validate_input(example, schema):
        print("oh no")
        exit(-1)
    # app = ThreatModel(example)
    content = example
    app = ThreatModel()
    app.run()
