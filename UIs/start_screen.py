import shutil
import requests
from tkinter import *
from PIL import Image, ImageTk
from utils.constants import *
from UIs.login_screen import LoginScreen
from UIs.register_screen import RegisterScreen

class StartScreen(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        self.is_offline = False
        self.current_background = Images.current_image
        self.next_background = Images.next_image

        self.get_random_background()

        # setting up the screen parameters
        root.geometry(ScreenConstants.screen_size)
        root.resizable(False, False)
        root.wm_title("Consumidos")

        # set the background image of the screen
        bkg = Image.open(Images.current_image)
        bkg_width, bkg_height = bkg.size
        logo = Image.open(Images.logo).convert("RGBA")
        logo_width, logo_heigth = logo.size
        width = int(bkg_width/2 - logo_width/2)
        bkg.paste(logo, (width, 200), logo)
        background_image = ImageTk.PhotoImage(bkg)
        background_label = Label(root, image = background_image)
        background_label.photo = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # log in button configuration
        log_in_label = Label(root)
        log_in_image = ImageTk.PhotoImage(Image.open(Images.log_in_button))
        log_in_label.photo = log_in_image
        log_in_button = Button(borderwidth = 0,
                            command=lambda: Frame(LoginScreen(root)).tkraise())
        log_in_button.grid(row=1, column=1)
        log_in_button.place(x = 85, y = 450)
        log_in_button.config(image = log_in_image)
        
        # register button configuration
        register_label = Label(root)
        register_image = ImageTk.PhotoImage(Image.open(Images.register_button))
        register_label.photo = register_image
        register_button = Button(borderwidth = 0, 
                                command=lambda: Frame(RegisterScreen(root)).tkraise())
        register_button.grid(row=1, column=2)
        register_button.place(x = 485, y = 450)
        register_button.config(image = register_image)

    def get_random_background(self):
        url = 'https://source.unsplash.com/800x600/?food'
        try:
            response = requests.get(url, stream=True)
            if response.status_code is 200:
                shutil.copyfile(self.next_background, self.current_background)
                with open(self.next_background, 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response
                im = Image.open(self.current_background)
                im.save(self.current_background, "PNG")
        except:
            self.is_offline = True