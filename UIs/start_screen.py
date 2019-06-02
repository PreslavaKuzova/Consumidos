from tkinter import *
from utils.constants import *

class StartScreen:
    def config():
        start_screen = Tk()
        start_screen.geometry(ScreenConstants.screen_size)
        start_screen.resizable(False, False)
        start_screen.mainloop()
