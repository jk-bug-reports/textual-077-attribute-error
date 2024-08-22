from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label


class SplashScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("splash screen")
    
    def on_mount(self) -> None:
        self.set_timer(2, self.next_screen)
    
    def next_screen(self) -> None:
        self.app.pop_screen()
