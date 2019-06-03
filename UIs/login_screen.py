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