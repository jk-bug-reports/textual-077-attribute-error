from enum import Enum
from textual.app import App

from darts.screens.game import GameScreen
from darts.screens.main_menu import MainMenuScreen
from darts.screens.splash import SplashScreen


class AppScreens(Enum):
    SPLASH = "splash"
    MAIN_MENU = "main_menu"
    GAME = "game"


class DartsApp(App):
    SCREENS = {
        AppScreens.SPLASH.name: SplashScreen,
        AppScreens.MAIN_MENU.name: MainMenuScreen,
        AppScreens.GAME.name: GameScreen,
    }

    def on_mount(self) -> None:
        self.push_screen(AppScreens.MAIN_MENU.name)
        # self.push_screen(AppScreens.SPLASH.name)
