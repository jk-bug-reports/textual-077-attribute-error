from typing import ClassVar
from uuid import uuid4

from rich.highlighter import Highlighter
from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding, BindingType
from textual.suggester import Suggester
from textual.validation import Validator
from textual.widgets import Header, Footer, ListView, ListItem, Input, Label
from textual import widgets as wgt
from textual.reactive import reactive


class Player:
    def __init__(self, name: str) -> None:
        self.id = uuid4()
        self.name = name


class PlayerInput(Input):
    BINDINGS: ClassVar[list[BindingType]] = [
        Binding("left", "cursor_left", "cursor left", show=False),
        Binding("ctrl+left", "cursor_left_word", "cursor left word", show=False),
        Binding("right", "cursor_right", "cursor right", show=False),
        Binding("ctrl+right", "cursor_right_word", "cursor right word", show=False),
        Binding("backspace", "delete_left", "delete left", show=False),
        Binding("home,ctrl+a", "home", "home", show=False),
        Binding("end,ctrl+e", "end", "end", show=False),
        Binding("delete,ctrl+d", "delete_right", "delete right", show=False),
        Binding("enter", "submit", "submit", show=False),
        Binding(
            "ctrl+w", "delete_left_word", "delete left to start of word", show=False
        ),
        Binding("ctrl+u", "delete_left_all", "delete all to the left", show=False),
        Binding(
            "ctrl+f", "delete_right_word", "delete right to start of word", show=False
        ),
        Binding("ctrl+k", "delete_right_all", "delete all to the right", show=False),
        Binding("down", "cursor_down", "cursor down", show=False),
    ]

    def __init__(self, player_name: str, player_id: str, **kwargs) -> None:
        super().__init__(player_name, **kwargs)
        self.player_id = player_id

    def on_mount(self) -> None:
        self.focus()

    def action_cursor_down(self) -> None:
        self.run_action("focus_next")


class DartsApp(App):
    ENABLE_COMMAND_PALETTE = False

    players: reactive[dict] = reactive({}, recompose=True)

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(
            key="question_mark",
            action="help",
            description="Show help screen",
            key_display="?",
        ),
        Binding(key="a", action="add_player", description="Add player"),
        Binding(key="d", action="delete_player", description="Delete player")
    ]

    def action_add_player(self) -> None:
        new_player = Player(None)
        self.players.update({new_player.id: new_player})
        
        self.mutate_reactive(DartsApp.players)

    @on(PlayerInput.Submitted)
    def update_players_s(self, event: PlayerInput.Submitted) -> None:
        player_id = event.input.player_id

        player = self.players.get(player_id)
        player.name = event.value

        self.mutate_reactive(DartsApp.players)

    def compose(self) -> ComposeResult:
        self.title = "Efidarts"
        yield Header()
        yield ListView(
            *[ListItem(PlayerInput(player.name, player.id, placeholder="Player name")) for player in self.players.values()]
        )
        yield wgt.Button("Begin game")
        yield Label(f"Player count: {len(self.players)}")
        yield wgt.Rule()
        # yield from [wgt.Pretty(player) for player in self.players]
        yield from [wgt.Pretty(f"{player.id}    {player.name}") for player in self.players.values()]
        yield Footer()


if __name__ == "__main__":
    app = DartsApp()
    app.run()
