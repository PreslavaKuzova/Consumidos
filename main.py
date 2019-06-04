from UIs.start_screen import *
from model.cron import *
from tkinter import *
from UIs.start_screen import StartScreen
from UIs.login_screen import LoginScreen

class App:
    @classmethod
    def start(cls):
        Cron.start_cron_job()
        root = Tk()
        start_screen = Frame(StartScreen(root))
        start_screen.tkraise()
        root.mainloop()
        

if __name__ == "__main__":
    App.start()
