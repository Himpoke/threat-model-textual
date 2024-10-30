"""Application providing functionality for OTM files"""
from textual.app import App, ComposeResult
from textual.widgets import Static, Header, TabbedContent, TabPane
from threatmodel import Project

class ThreatModel(App):
    """Textual threat model app."""

    CSS_PATH = "threatmodel.tcss"
    
    def __init__(self, content: dict):
        super().__init__()
        self.title = "Open Threat Model Editor"
        self.tabbedcontent = None
        self.tab_project = None
        self.content = content

    def compose(self) -> ComposeResult:
        """Compose our UI."""
        yield Header()
        self.tabbedcontent = TabbedContent(id="project_viewer", initial="project")

        with self.tabbedcontent:
            with TabPane("Project", id="project"):
                yield Project(id="project",content=self.content["project"])
            with TabPane("Assets", id="assets"):
                yield Static("id, name, description, risk")
                yield Static("risk: confidentiality, integrity, availability, comment")
            with TabPane("Trust Zones", id="trustZones"):
                yield Static(
                    "id, name, type, description, risk, parent, representation, attributes"
                )
            with TabPane("Components", id="components"):
                yield Static(
                    "id, name, description, type, parent, representations, assets,"+
                        "threats, tags, attributes"
                )
            with TabPane("DataFlows", id="dataflows"):
                yield Static(
                    "id, name, description, bidirectional, source, "+
                        "destination, assets, threats, tags, attributes"
                )
