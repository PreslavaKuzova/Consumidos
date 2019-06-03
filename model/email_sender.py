import smtplib, ssl, datetime

class EmailSender:
    
    def send_simple_email(text):
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("consumidos.info@gmail.com", "presiilinalyudmi123")
        server.sendmail(
          "consumidos.info@gmail.com", 
          #TODO : get receiver email from database
          "ilina.pavllova@gmail.com", 
          f"""\
Subject: {text} """)
        server.quit()

    @classmethod
    def send_reminder_email(cls, food):
        #TODO : check if there is expiring food, then send email
        pass