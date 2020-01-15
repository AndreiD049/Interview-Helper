import json
import os
import sys
import src.utils as utils
from src.Exceptions import ConfigError
from src.typing_page.TypingPage import TypingPage
from src.validators import ValidatorErrorChecking, ValidatorTyping


__def_config = {
    "screens": [
        {
            "name": "StartScreen"
        },
        {
            "name": "TypingScreen"
        }
    ],
    "TypingTestsFolder": "./data/typing/",
    "ErrorCheckingTestsFolder": "./data/error_checking/",
    "resultsFolder": "./data/results/"
}

_screens = {
    "StartScreen",
    "TypingScreen",
    "ErrorCheckingScreen"
}

_validators = {
    "TypingScreen":  ValidatorTyping,
    "ErrorCheckingScreen": ValidatorErrorChecking 
}

class Controller:

    def __init__(self, view):
        self.config = self.getConfig()
        self.curIdx = 0
        self.view = view
        
        self._screen_hooks = {
            "StartScreen": self.goToMainScreen,
            "TypingScreen": self.initTypingScreen
        }

    def setModel(self, model):
        self.model = model

    def getConfig(self):
        # Check if config file is available
        if os.path.exists("config.json"):
            fp = open("config.json", "r")
            config = json.load(fp)
            # if there is an unvalid screen, throw error
            self.checkScreens(config["screens"])
            return config
        else:
        # else use default config
            return __def_config

    @staticmethod
    def checkScreens(screens):
        for screen in screens:
            if screen["name"] not in _screens:
                raise ConfigError(f"Configuration file error. Screen {screen['name']} not in the list of valid screend.\n"
                                  f"Valid screens: {', '.join(_screens)}")

    def nextScreen(self):
        """
        calls the initialization function for the next screen
        """
        l = len(self.config["screens"])
        self.curIdx = self.curIdx + 1 if (self.curIdx + 1) < l else 0
        self._screen_hooks[self.config["screens"][self.curIdx]["name"]]()
        self.view.ui.stackedWidget.setCurrentIndex(self.curIdx)
        self.view.ui.stackedWidget.currentWidget().startUp()


    def initTypingScreen(self):
        """
        initalizes the Typing screen
        """
        TypingPage(self.view)

    def goToMainScreen(self):
        self.view.ui.stackedWidget.setCurrentIndex(0)

    def getRandomFiles(self, path, n):
        """
        Returns a list of paths to random files from @path
        """
        # get the current screen name
        screen = self.config["screens"][self.curIdx]["name"]
        return utils.select_n_valid_files(_validators[screen].validate, n, path, "json")


if __name__ == "__main__":
    pass