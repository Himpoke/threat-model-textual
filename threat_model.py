"""Application providing functionality for OTM files"""
import json
import jsonschema
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Static, TabbedContent, TabPane, Input
from textual.containers import Vertical
from schema_fetcher import read_otm

content = {}

class Project(Vertical):
  """ project data """
  def compose(self) -> ComposeResult:
    yield Static("Name")
    yield Input("", id="project_name")
    yield Static("Description")
    yield Input("", id="project_description")
    yield Static("Owner")
    yield Input("", id="project_owner")
    yield Static("Owner Contact")
    yield Input("", id="project_owner_contact")

  def load_content(self, content) -> None:
    self.query_one("#project_name",Input).value = content['name']
    self.query_one("#project_description",Input).value = content['description']

class ThreatModel(App):
  """Textual threat model app."""
  CSS_PATH = "threat_model.tcss"

  # def __init__(self, content):
    # self.content = content

  def compose(self) -> ComposeResult:
    """Compose our UI."""
    yield Header()
    self.title = "Open Threat Model Editor"
    self.tabbedcontent = TabbedContent(id="project_viewer", initial="project")

    with self.tabbedcontent:
      with TabPane("Project", id="project"):
        self.tab_project = Project()
        yield self.tab_project
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
    self.log("I know this works, just not why it doesn't print")

  def on_mount(self):
    self.log("what")
    self.tab_project.load_content(content['project'])

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
  schema = read_otm()
  example = read_example()
  if not validate_input(example,schema):
    print("oh no")
    exit(-1)
  #app = ThreatModel(example)
  content = example
  app = ThreatModel()
  app.run()
