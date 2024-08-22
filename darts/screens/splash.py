from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label, Static

from darts.assets.darts_ascii_art import DARTS_ASCII_ART


class SplashScreen(Screen):
    CSS_PATH = "splash.tcss"

    def compose(self) -> ComposeResult:
        self.ascii_art_wgt = Static(DARTS_ASCII_ART, id="splash_ascii_art")
        yield self.ascii_art_wgt
    
    def on_mount(self) -> None:
        self.ascii_art_wgt.styles.animate("opacity", value=0.0, duration=2.0, easing="in_quart")
        self.set_timer(2, self.next_screen)

    def next_screen(self) -> None:
        self.app.pop_screen()
