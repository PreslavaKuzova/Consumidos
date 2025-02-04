from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from utils.constants import *
from UIs.error_screen import ErrorScreen
from UIs.user_products_screen import UserProductsScreen
from utils.errors import *
from controllers.login_controller import LoginController

class LoginScreen(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        
        self.is_offline = False
        self.current_background = Images.current_image
        self.next_background = Images.next_image

        root.geometry(ScreenConstants.screen_size)
        root.resizable(False, False)
        root.wm_title('Login Screen')
    
        # set the background image of the screen, draw the box and paste the transparent logo
        bkg_image = Image.open(Images.current_image)
        bkg_width, bkg_height = bkg_image.size
        ImageDraw.Draw(bkg_image).rectangle(
            ((bkg_width/2-200, bkg_height/2-100), (bkg_width/2+200, bkg_height/2+200)), fill="white")
        logo = Image.open(Images.login).convert("RGBA")
        logo_width, logo_heigth = logo.size
        width = int(bkg_width/2 - logo_width/2)
        bkg_image.paste(logo, (width, 50), logo)
        background_image = ImageTk.PhotoImage(bkg_image)
        background_label = Label(root, image = background_image)
        background_label.photo = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        username = ""

        # set the login functionality
        main_frame = Frame(root, bg = "white")
        main_frame.grid(row=0, column=0, rowspan=3, columnspan=3)
        username = Label(main_frame, text="Please, provide your username: ", bg='white', 
                font = ("Courier", 15), pady = 20)
        username.grid(row = 0, column = 1)
        username_login_entry = Entry(main_frame, bg='white', font = ("Courier", 18))
        username_login_entry.grid(row = 1, column = 1)

        # placing the new frame in the middle of the screen
        main_frame.place(x = 215, y = 270)
        
        
        log_in_label = Label(root)
        log_in_image = ImageTk.PhotoImage(Image.open(Images.log_in_button))
        log_in_label.photo = log_in_image
        log_in_button = Button(text="hello", borderwidth = 0, bg = "white",
                            command=lambda: self.login(root, username_login_entry.get()))
        log_in_button.grid(row=4, column=1)
        log_in_button.place(x = 283, y = 430)
        log_in_button.config(image = log_in_image)

    def login(self, root, username):
        try:
            LoginController.sign_in(username)
        except InvalidUsernameError:
            new_root = Toplevel()
            error_message = ErrorScreen(new_root, "No such username! Please register!")
        except DatabaseConnectionError:
            new_root = Toplevel()
            error_message = ErrorScreen(new_root, "Database connection error. Please try again!")
        else:
            Frame(UserProductsScreen(root)).tkraise()