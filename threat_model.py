"""Application providing functionality for OTM files"""
import json
import jsonschema
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Static, TabbedContent, TabPane, Input
from textual.containers import VerticalScroll
from schema_fetcher import read_otm

class Project(VerticalScroll):
  """ project data """
  def compose(self) -> ComposeResult:
    yield Input("Name", id="project_name")
    yield Static("project data")

class ThreatModel(App):
  """Textual threat model app."""
  CSS_PATH = "threat_model.tcss"
  def compose(self) -> ComposeResult:
    """Compose our UI."""
    yield Header()
    self.title = "Open Threat Model Editor"


    with TabbedContent(id="project_viewer", initial="project"):
      with TabPane("Project", id="project"):
        yield Project()
        with TabPane("Assets", id="assets"):
          yield Static("id, name, description, risk")
          yield Static("risk: confidentiality, integrity, availability, comment")
          with TabPane("Trust Zones", id="trustZones"):
            yield Static("id, name, type, description, risk, parent, representation, attributes")
            with TabPane("Components", id="components"):
              yield Static("id, name, description, type, parent, representations, assets, threats, tags, attributes")
            with TabPane("DataFlows", id="dataflows"):
              yield Static("id, name, description, bidirectional, source, destination, assets, threats, tags, attributes")

    @on(TabbedContent.TabActivated, "#project_viewer")
    def on_tabs_tab_activated(self, event: TabbedContent.TabActivated) -> None:
      """ event handler? """
      print("I know this works, just not why it doesn't print")

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
    example = read_example()
    if not validate_input(example,schema):
      print("oh no")
    else:
      print("fetched data")
