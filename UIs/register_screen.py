from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from UIs.error_screen import ErrorScreen
from UIs.user_products_screen import UserProductsScreen
from controllers.register_controller import RegisterController
from utils.constants import *
from utils.errors import *

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
        main_frame = Frame(root, bg = "white")
        main_frame.grid(row=0, column=0, rowspan=3, columnspan=3)
        username = Label(main_frame, text="Please, choose username:", bg='white', 
                font = ("Courier", 15), pady = 20)
        username.grid(row = 0, column = 1)
        
        username_register_entry = Entry(main_frame, bg='white', font = ("Courier", 18))
        username_register_entry.grid(row = 1, column = 1)
        
        email = Label(main_frame, text="Please, enter your email:", bg='white', 
                font = ("Courier", 15), pady = 20)
        email.grid(row = 2, column = 1)
        
        email_register_entry = Entry(main_frame, bg='white', font = ("Courier", 18))
        email_register_entry.grid(row = 3, column = 1)

        # placing the new frame in the middle of the screen
        main_frame.place(x = 250, y = 220)
        
        register_label = Label(root)
        register_image = ImageTk.PhotoImage(Image.open(Images.log_in_button))
        register_label.photo = register_image
        register_button = Button(text="hello", borderwidth = 0, bg = "white",
                            command=lambda: self.register(root, username_register_entry.get(), email_register_entry.get()))
        register_button.grid(row=4, column=1)
        register_button.place(x = 283, y = 430)
        register_button.config(image = register_image)
        
    def register(self, root, username, email):
        try:
            RegisterController.sign_up(username, email)
        except UsernameAlreadyExistsError:
            new_root = Toplevel()
            error_message = ErrorScreen(new_root, "Unfortunately this username is already taken!")
        except EmailAlreadyExistsError:
            new_root = Toplevel()
            error_message = ErrorScreen(new_root, "Sorry! Somebody already uses this email.")
        except DatabaseConnectionError:
            new_root = Toplevel()
            error_message = ErrorScreen(new_root, "Database connection error. Please try again!")
        else:
            Frame(UserProductsScreen(root)).tkraise()