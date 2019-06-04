from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from utils.constants import *

class RegisterScreen(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        
        self.is_offline = False
        self.current_background = Images.current_image
        self.next_background = Images.next_image

        root.geometry(ScreenConstants.screen_size)
        root.resizable(False, False)
        root.wm_title('Register Screen')

        # set the background image of the screen
        bkg_image = Image.open(Images.current_image)
        bkg_width, bkg_height = bkg_image.size
        ImageDraw.Draw(bkg_image).rectangle(
            ((bkg_width/2-200, bkg_height/2-100), (bkg_width/2+200, bkg_height/2+200)), fill="white")
        logo = Image.open(Images.register).convert("RGBA")
        logo_width, logo_heigth = logo.size
        width = int(bkg_width/2 - logo_width/2)
        bkg_image.paste(logo, (width, 50), logo)
        background_image = ImageTk.PhotoImage(bkg_image)
        background_label = Label(root, image = background_image)
        background_label.photo = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # add register functionality