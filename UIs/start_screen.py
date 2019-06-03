import shutil
import requests
from tkinter import *
from PIL import Image, ImageTk
from utils.constants import *
from UIs.login_screen import LoginScreen

class StartScreen(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        self.is_offline = False
        self.current_background = Images.current_image
        self.next_background = Images.next_image

        #gets random background, to be removed and added to the controller later
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

        # setting up the screen parameters
        
        root.geometry(ScreenConstants.screen_size)
        root.resizable(False, False)
        root.wm_title("Consumidos")

        # set the background image of the screen
        filename = PhotoImage(file = Images.current_image)
        background_label = Label(root, image = filename)
        background = Label(image = filename)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        
        logo = ImageTk.PhotoImage(file = Images.logo)
        panel = Label(image = logo)
        panel.grid(row = 0, column = 1)
        panel.place(x = 230, y = 200)

        # log in button configuration
        log_in_button = Button(text="hello", borderwidth = 0,
                            command=lambda: self.open_login_screen())
        log_in_button.grid(row=1, column=1)
        log_in_button.place(x = 85, y = 450)
        # img_log_in = PhotoImage(file = Images.log_in_button)
        # log_in_button.config(image = img_log_in)

        # register button configuration
        register_button = Button(text = 'hello1', borderwidth = 0, 
                                command=lambda: self.open_login_screen())
        register_button.grid(row=1, column=2)
        register_button.place(x = 485, y = 450)
        # img_register = PhotoImage(file = Images.register_button)
        # register_button.config(image = img_register)

    def open_login_screen(self):
        root = Toplevel()
        login_screen = LoginScreen(root)