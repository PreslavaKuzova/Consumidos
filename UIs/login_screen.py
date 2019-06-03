from tkinter import *
from PIL import Image, ImageTk
from utils.constants import *

class LoginScreen(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        
        self.is_offline = False
        self.current_background = Images.current_image
        self.next_background = Images.next_image

        root.geometry(ScreenConstants.screen_size)
        root.resizable(False, False)
        root.wm_title('Login Screen')

        # set the background image of the screen
        bkg_image = Image.open(Images.current_image)
        background_image = ImageTk.PhotoImage(bkg_image)
        background_label = Label(root, image = background_image)
        background_label.photo = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # set the login functionality