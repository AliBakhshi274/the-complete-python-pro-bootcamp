import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

class EmailManager:
    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message
        self.addr_to =  os.environ['addr_to']
        self.password = os.environ['password']
        self.addr_from = os.environ['addr_from']
        self.send_mail()

    def send_mail(self):
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=self.addr_from, password=self.password)
            connection.sendmail(self.addr_from, self.addr_to, msg=f'Subject:{self.subject}\n\n{self.message}')
















