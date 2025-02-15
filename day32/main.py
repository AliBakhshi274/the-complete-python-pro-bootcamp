import pandas
import datetime as dt
import smtplib
import random

def send_email(to_addr, msg_body):
    from_addr = 'aliard.bks@gmail.com'
    password = 'kdbh fovj odwn bmhe'
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=from_addr, password=password)
        connection.sendmail(from_addr, to_addr, msg=f'Subject:Congratulations!\n\n{msg_body}')
def get_msg_body(contact_name) -> str:
    with open(f'letter_templates/letter_{random.randint(1, 3)}.txt', 'r') as file:
        msg_body = file.read()
        return msg_body.replace('[NAME]', contact_name)


d = pandas.read_csv("birthdays.csv")
data_list = d.to_dict(orient="records")

today = dt.datetime.now()
for data_dict in data_list:
    if (data_dict['month'], data_dict['day']) == (today.month, today.day):
        msg_body = get_msg_body(data_dict['name'])
        send_email(data_dict['email'], msg_body)










