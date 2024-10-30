"""list of tags with controls for adding and removing tags"""
from textual import on
from textual.app import ComposeResult
from textual.widget import Widget
from textual.containers import Horizontal, Vertical
from textual.widgets import DataTable, Button

class TagList(Widget):
    """taglist class"""
    def __init__(
            self,
            content: list[str],
            name: str | None = None,
            id: str | None = None,
            classes: str | None = None,
            disabled: bool = False):
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self.content = content

    def compose(self) -> ComposeResult:
        """Compose the UI."""
        yield Horizontal(DataTable(id="tags_table"),
                         Vertical(Button(label="add",id="tags_add"),
                                  Button(label="del",id="tags_del")))

    def on_mount(self) -> None:
        """Display data"""
        tag_table = self.query_one("#tags_table", DataTable)
        tag_table.cursor_type = "row"
        tag_table.add_column("tag")
        print(self.content)
        for tag in self.content:
            tag_table.add_row(tag)

    @on(Button.Pressed, "#tags_add")
    def add_button_press(self) -> None:
        tag_table = self.query_one("#tags_table", DataTable)
        tag_table.add_row("newvalue")

    @on(Button.Pressed, "#tags_del")
    def del_button_press(self) -> None:
        tag_table = self.query_one("#tags_table", DataTable)
        row_key, _ = tag_table.coordinate_to_cell_key(tag_table.cursor_coordinate)
        tag_table.remove_row(row_key)
