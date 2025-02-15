# import smtplib
#
# my_email = "aliard.bks@gmail.com"
# password = "kdbh fovj odwn bmhe"
# mail_to = "polepey147@shouxs.com"
#
# with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=mail_to, msg="Subject:Hello\n\nThis is the body")

# import datetime as dt
#
# date_of_birth = dt.datetime(year=1998, month=7, day=18)
# print(date_of_birth)

import random
import smtplib
import datetime as dt

my_email = 'aliard.bks@gmail.com'
password = 'kdbh fovj odwn bmhe'
email_to = 'polepey147@shouxs.com'

split_quote = []

def load_quote():
    global split_quote
    with open("quotes.txt") as file:
        quotes_list = file.readlines()
        quote = random.choice(quotes_list)
        split_quote = quote.split('-')
def get_name():
    return split_quote[1]
def get_text():
    return split_quote[0]
def send_email():
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        date_time = dt.datetime.now()
        if date_time.day == 15:
            connection.sendmail(my_email, email_to, f"Subject:{get_name()}\n\n{get_text()}")

load_quote()
send_email()










































