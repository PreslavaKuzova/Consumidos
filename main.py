from UIs.start_screen import *
from model.cron import *

class Application:
    @classmethod
    def start(cls):
        Cron.start_cron_job()
        start_screen = StartScreen()
        start_screen.config()

if __name__ == "__main__":
    Application.start()