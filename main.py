from tkinter import *
from UIs.start_screen import StartScreen

class App:
    @classmethod
    def start(cls):
        root = Tk()
        app = StartScreen(root)
        root.mainloop()
        

if __name__ == "__main__":
    App.start()