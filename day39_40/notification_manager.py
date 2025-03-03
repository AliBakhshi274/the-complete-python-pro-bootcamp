import os
import smtplib

from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.email_password = os.environ["EMAIL_PASSWORD"]
        self.from_addr = os.environ["FROM_ADDR"]

    def send_mail(self, recipients_data, message):
        with smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDR"], int(os.environ["EMAIL_PORT_NUM"])) as connection:
            connection.starttls()
            print("Sending email...")
            connection.login(user=self.from_addr, password=self.email_password)
            for recipient in recipients_data:
                to_name = recipient["whatIsOurFirstName?"]
                to_family_name = recipient["whatIsYourLastName?"]
                to_email_addr = recipient["whatIsYourEmail?"]
                connection.sendmail(self.from_addr, to_email_addr , msg=f"Subject:FANTASTIC {to_name} {to_family_name}!\n\n{message}")
























