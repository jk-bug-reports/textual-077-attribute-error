from typing import ClassVar

from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding, BindingType
from textual.widgets import Header, Footer, ListView, ListItem, Input, Label
from textual import widgets as wgt
from textual.reactive import reactive


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

    def on_mount(self) -> None:
        self.focus()

    def action_cursor_down(self) -> None:
        self.run_action("focus_next")


class DartsApp(App):
    ENABLE_COMMAND_PALETTE = False

    currently_focused = reactive("")
    players: reactive[list[str]] = reactive([""], recompose=True)

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
        self.players.append("")
        self.mutate_reactive(DartsApp.players)

    @on(Event.Focus)

    @on(PlayerInput.Changed)
    def update_players(self, event: PlayerInput.Changed) -> None:
        pass

    @on(PlayerInput.Submitted)
    def update_players(self, event: PlayerInput.Submitted) -> None:
        pass

    def compose(self) -> ComposeResult:
        self.title = "Efidarts"
        yield Header()
        yield ListView(
            *[ListItem(PlayerInput(player, placeholder="Player name")) for player in self.players]
        )
        yield wgt.Button("Begin game")
        yield Label(f"Player count: {len(self.players)}")
        yield wgt.Rule()
        yield wgt.Pretty(self.players)
        # yield wgt.Label(f"{self.focused.name if self.focused else 'no focus'}")
        yield wgt.Label(f"{self.currently_focused}")
        yield Footer()


if __name__ == "__main__":
    app = DartsApp()
    app.run()
