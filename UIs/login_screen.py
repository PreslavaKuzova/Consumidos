from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from utils.constants import *
from UIs.error_screen import ErrorScreen
from utils.errors import *

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
        password = ""

        # set the login functionality
        username_label = Label(root, text="Username * ", bg='white')
        username_label.grid(row = 0, column = 1)
        username_login_entry = Entry(root, bg='white')
        username_login_entry.grid(row = 1, column = 1)
        
        password_label = Label(root, text="Password * ", bg='white')
        password_label.grid(row = 2, column = 1)
        password_login_entry = Entry(root, show='*', bg='white')
        password_login_entry.grid(row = 3, column = 1)
        
        try:
            log_in_button = Button(text="hello", borderwidth = 0,
                               command=lambda: print(f'{username_login_entry.get()} {password_login_entry.get()}'))
            log_in_button.grid(row=4, column=1)
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
            new_root = Toplevel()
            error_message = ErrorScreen(new_root, "Database connection error. Please try again!")

        
