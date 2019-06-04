import smtplib, ssl, datetime, sys, os
from utils.constants import EmailConstants as const
from database.queries import *

class EmailSender:

    @classmethod
    def send_email(cls, receiver, text):
        server = smtplib.SMTP_SSL(const.smtp_server, const.port)
        server.login(const.sender_email, const.sender_password)
        server.sendmail(
          const.sender_email,
          receiver, 
          f"""\
Subject: Foods expiring!
{text} """)
        server.quit()

    # @classmethod
    # def send_reminder_email(cls, receiver):
    #     expiring_foods = db.get_expiring_foods()
    #     if len(expired_foods) != 0:
    #         text = f'Don\'t forget to eat {','.join(expired_foods)}, their shelf life expires in one day! Have a nice day :)'
    #         send_simple_email(receiver, text)