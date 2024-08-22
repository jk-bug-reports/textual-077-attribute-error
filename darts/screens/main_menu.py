from textual import on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, OptionList
from textual.widgets.option_list import Option


class MainMenuScreen(Screen):
    CSS_PATH = "main_menu.tcss"

    @on(OptionList.OptionSelected)
    async def on_option_selected(self, event):
        match event.option.id:
            case "exit":
                self.app.exit()

    def compose(self) -> ComposeResult:
        yield Header()
        yield OptionList(
            Option("Start new game", id="new_game"),
            Option("Edit players", id="edit_players"),
            Option("Exit", id="exit"),
            id="main_menu__option_list"
        )
