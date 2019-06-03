import shutil
import requests
from tkinter import *
from utils.constants import *
from PIL import Image, ImageTk


class StartScreen:
    def __init__(self):
        self.is_offline = False
        self.current_background = Images.current_image
        self.next_background = Images.next_image

    def get_random_background(self):
        #TODO put this in the controller
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

    @staticmethod
    def main_colour_black_or_white(infile, numcolors=3, resize=150):
        #TODO find the colour and put this is the controller
        image = Image.open(infile)
        image = image.resize((resize, resize))
        result = image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)
        result.putalpha(0)
        colors = result.getcolors(resize*resize)
        print(colors)
        r = colors[0][1][0]
        g = colors[0][1][1]
        b = colors[0][1][1]
        return ((r * 0.299) + (g * 0.587) + (b * 0.114)) > 186
    
    def config(self):
        self.get_random_background()
        self.colour = self.main_colour_black_or_white(self.current_background)
        print(self.colour)

        start_screen = Tk()
        start_screen.geometry(ScreenConstants.screen_size)
        start_screen.resizable(False, False)
        start_screen.wm_title('Consumidos')
        
        start_screen.wm_attributes('-alpha', 0.7)

        C = Canvas(start_screen, bg="blue", height=250, width=300)
        filename = PhotoImage(file = self.current_background)
        background_label = Label(start_screen, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        background = Label(image = filename)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        
        img = ImageTk.PhotoImage(Image.open(Images.logo))
        panel = Label(image = img)
        panel.grid(row = 0, column = 1)

        log_in_button = Button(background, borderwidth = 0)
        log_in_button.grid(row=1, column=1)
        log_in_button.place(x = 340, y = 160)
        img_log_in = PhotoImage(file = Images.log_in_button)
        log_in_button.config(image = img_log_in)

        register_button = Button(start_screen, borderwidth = 0)
        register_button.grid(row=2, column=1)
        register_button.place(x = 340, y = 250)
        img_register = PhotoImage(file = Images.register_button)
        register_button.config(image = img_register)

        start_screen.mainloop()
