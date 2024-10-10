from textual.app import App, ComposeResult
from textual.widgets import Collapsible, Label

class ThreatModel(App):
    """Textual threat model app."""
    CSS_PATH = "threat-model.tcss"
    def compose(self) -> ComposeResult:
        """Compose our UI."""
        with Collapsible():
            yield Label("Hello world!")

if __name__ == "__main__":
    ThreatModel().run()
