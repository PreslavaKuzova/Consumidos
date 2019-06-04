from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from utils.constants import *

class ErrorScreen(Frame):
    def __init__(self, root, message):
        Frame.__init__(self, root)
    
        root.geometry(ScreenConstants.error_screen_size)
        root.resizable(False, False)
        root.wm_title('Oops. Something went wrong!')

        password_label = Label(root, text = message)
        password_label.grid(row = 0, column = 1)