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

        error_image = Image.open(Images.error).convert("RGBA")
        logo_width, logo_heigth = error_image.size
        width = int(300/2 - logo_width/2)
        root.paste(error_image, (width, 50), error_image)

        password_label = Label(root, text = message, font = ("Courier", 15))
        password_label.grid(row = 0, column = 1)