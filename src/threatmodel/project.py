"""Controls and logic to display and save project data"""
from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Input, Static
from threatmodel.taglist import TagList
from threatmodel.attributelist import AttributeList


class Project(VerticalScroll):
    """project data"""
    
    def __init__(
        self,
        *,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        disabled: bool = False,
        content: dict
    ):
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self.content = content
        self.project_id = content['id']

    def compose(self) -> ComposeResult:
        """Build controls"""
        yield Horizontal(Static("Name"), Input("", id="project_name"))
        yield Horizontal(Static("Description"), Input("", id="project_description"))
        yield Horizontal(Static("Owner"), Input("", id="project_owner"))
        yield Horizontal(Static("Owner Contact"), Input("", id="project_owner_contact"))
        tags: list[str] = []
        if "tags" in self.content:
            tags = self.content["tags"]
        attrs: dict = {}
        if "attributes" in self.content:
            attrs = self.content["attributes"]

        yield Horizontal(
                Horizontal(
                        Static("Tags"),
                        TagList(id="project_tag",content=tags),
                ),
                Horizontal(
                        Static("Attributes"),
                        AttributeList(id="project_attr",content=attrs),
                )
        )

    def on_mount(self) -> None:
        """Display passed data"""
        self.query_one("#project_name", Input).value = self.content["name"]
        self.query_one("#project_description", Input).value = self.content["description"]
        self.query_one("#project_owner", Input).value = self.content["owner"]
        self.query_one("#project_owner_contact", Input).value = self.content["ownerContact"]
