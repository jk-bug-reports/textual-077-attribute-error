from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label


class MainMenuScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("main menu")
