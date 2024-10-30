"""Controls and logic to display and save project data"""
from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Input, DataTable, Static
from textual.widget import Widget

class Project(VerticalScroll):
    """project data"""
    
    def __init__(
        self,
        *children: Widget,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        disabled: bool = False,
    ):
        super().__init__(*children, name=name, id=id, classes=classes, disabled=disabled)
        self.project_id = None

    def compose(self) -> ComposeResult:
        yield Horizontal(Static("Name"), Input("", id="project_name"))
        yield Horizontal(Static("Description"), Input("", id="project_description"))
        yield Horizontal(Static("Owner"), Input("", id="project_owner"))
        yield Horizontal(Static("Owner Contact"), Input("", id="project_owner_contact"))
        yield Horizontal(
            Static("Tags"),
            DataTable(id="project_tags"),
            Static("Attributes"),
            DataTable(id="project_attributes"),
        )

    def load_content(self, content) -> None:
        """Display passed data to the window"""
        self.project_id = content["id"]
        self.query_one("#project_name", Input).value = content["name"]
        self.query_one("#project_description", Input).value = content["description"]
        self.query_one("#project_owner", Input).value = content["owner"]
        self.query_one("#project_owner_contact", Input).value = content["ownerContact"]
        tag_table = self.query_one("#project_tags", DataTable)
        tag_table.add_columns("tag")
        if "tags" in content:
            for tag in content["tags"]:
                tag_table.add_row(tag)
        attr_table = self.query_one("#project_attributes", DataTable)
        attr_table.add_columns("key", "value")
        if "attributes" in content:
            for attr in content["attributes"]:
                attr_table.add_row(attr, content["attributes"][attr])
