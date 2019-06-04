import smtplib, ssl, datetime, sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f'{path}/../utils')
sys.path.insert(0, f'{path}/../database')
from constants import EmailConstants as const
from queries import *

class EmailSender:
    
    def send_simple_email(text):
        server = smtplib.SMTP_SSL(const.smtp_server, const.port)
        server.login(const.sender_email, const.sender_password)
        server.sendmail(
          const.sender_email, 
          #TODO : get receiver email from database
          "ilina.pavllova@gmail.com", 
          f"""\
Subject: {text} """)
        server.quit()

    @classmethod
    def send_reminder_email(cls, food):
        #TODO : check if there is expiring food, then send email
        pass