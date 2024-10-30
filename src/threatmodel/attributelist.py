"""list of key-value attributes with controls for adding and removing"""
from textual import on
from textual.app import ComposeResult
from textual.widget import Widget
from textual.containers import Horizontal, Vertical
from textual.widgets import DataTable, Button

class AttributeList(Widget):
    """attributelist class"""
    def __init__(
            self,
            content: dict,
            name: str | None = None,
            id: str | None = None,
            classes: str | None = None,
            disabled: bool = False):
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self.content = content

    def compose(self) -> ComposeResult:
        """Compose the UI."""
        yield Horizontal(DataTable(id="attr_table"),
                         Vertical(Button(label="add",id="attr_add"),
                                  Button(label="del",id="attr_del")))

    def on_mount(self) -> None:
        """Display data"""
        attr_table = self.query_one("#attr_table", DataTable)
        attr_table.cursor_type = "row"
        attr_table.add_columns("key","value")
        print(self.content)
        for attr in self.content:
            attr_table.add_row(attr,self.content[attr])

    @on(Button.Pressed, "#attr_add")
    def add_button_press(self) -> None:
        attr_table = self.query_one("#attr_table", DataTable)
        attr_table.add_row("newvalue")

    @on(Button.Pressed, "#attr_del")
    def del_button_press(self) -> None:
        attr_table = self.query_one("#attr_table", DataTable)
        row_key, _ = attr_table.coordinate_to_cell_key(attr_table.cursor_coordinate)
        attr_table.remove_row(row_key)
