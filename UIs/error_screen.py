from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from utils.constants import *

class ErrorScreen(Frame):
    def __init__(self, root, message):
        Frame.__init__(self, root)
    
        root.geometry(ScreenConstants.error_screen_size)
        root.resizable(False, False)
        root.wm_title('Oops. Something went wrong!')
        root.configure(background = "#D3D3D3")

        error_message = Message(root, text= message, font = ("Courier", 11), 
                background = "#D3D3D3", justify="center", pady = 50)
        error_message.pack()