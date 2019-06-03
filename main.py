from UIs.start_screen import *

class Application:
    @classmethod
    def start(cls):
        start_screen = StartScreen()
        start_screen.config()

if __name__ == "__main__":
    Application.start()