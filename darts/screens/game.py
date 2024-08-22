from uuid import uuid4

from textual import on
from textual.screen import Screen
from textual.app import App, ComposeResult
from textual import widgets as wgt
from textual.reactive import reactive
from textual.events import Key


class Player:
    def __init__(self, name: str) -> None:
        self.id = uuid4()
        self.name = name

        self.run_action("focus_next")


class GameScreen(Screen):
    players_text: reactive[str] = reactive("foobar", recompose=True)
    players: reactive[dict] = reactive({}, recompose=True)

    SUB_TITLE = "Player settings"

    @on(Key)
    def handle_ctrl_s(self, event: Key) -> None:
        if event.name != "ctrl_s":
            return
        print("Keypress")

    def action_add_player(self) -> None:
        new_player = Player(None)
        self.players.update({new_player.id: new_player})

        self.mutate_reactive(self.players)

    def compose(self) -> ComposeResult:
        yield wgt.Header()
        yield wgt.Label("Input player names in new lines. Press CTRL+S when done.", expand=True)
        yield wgt.TextArea(show_line_numbers=True, text="")

