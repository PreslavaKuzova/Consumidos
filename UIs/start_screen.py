from tkinter import *
from utils.constants import *

class StartScreen:
    def get_random_photo():
        pass

    def config():
        start_screen = Tk()
        start_screen.geometry(ScreenConstants.screen_size)
        start_screen.resizable(False, False)
        start_screen.wm_title('Consumidos')
        
        C = Canvas(start_screen, bg="blue", height=250, width=300)
        filename = PhotoImage(file = Images.background)
        background_label = Label(start_screen, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        log_in_button = Button(start_screen)
        log_in_button.grid(row=0, column=1)
        log_in_button.place(x = 330, y = 120)
        img_log_in = PhotoImage(file = Images.log_in_button)
        log_in_button.config(image = img_log_in)

        register_button = Button(start_screen)
        register_button.grid(row=1, column=1)
        register_button.place(x = 330, y = 230)
        img_register = PhotoImage(file = Images.register_button)
        register_button.config(image = img_register)

        start_screen.mainloop()
