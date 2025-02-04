import glob
import os

class ScreenConstants:
    screen_size = "800x600"
    error_screen_size = "300x150"
    font = "Helvetica"

class Images:
    log_in_button = "utils/buttons/button_log_in.png"
    register_button = "utils/buttons/button_register.png"
    logo = "utils/images/consumidos_logo.png"
    login = "utils/images/login_logo.png"
    register = "utils/images/register_logo.png"
    error = "utils/images/error_image.png"
    user_products = "utils/images/products_logo.png"
    current_image = "utils/images/current.png"
    next_image = "utils/images/next.png"

class EmailConstants:
    port = 465
    smtp_server = "smtp.gmail.com" 
    sender_email = "consumidos.info@gmail.com"
    sender_password = "presiilinalyudmi123"