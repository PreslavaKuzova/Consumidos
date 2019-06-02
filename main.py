from UIs.start_screen import *

class Application:
    @classmethod
    def start(cls):
        StartScreen.config()

if __name__ == "__main__":
    Application.start()