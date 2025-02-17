import smtplib
import time
import requests
from datetime import datetime

MY_LAT = 49 # Your latitude
MY_LONG = -42 # Your longitude

def send_mail(to_addr, msg):
    from_addr = 'aliard.bks@gmail.com'
    password = 'kdbh fovj odwn bmhe'
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(from_addr, password)
    connection.sendmail(from_addr, to_addr, msg)

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

print(iss_latitude, iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def calculate(my_lat, my_lng, iss_lat, iss_lng) -> bool:
    print((my_lat - iss_lat) + (my_lng - iss_lng))
    return -20 < (my_lat - iss_lat) + (my_lng - iss_lng) < 20

while True:
    is_currently_dark = sunset <= time_now.hour or 0 <= time_now.hour <= sunrise
    print(calculate(MY_LAT, MY_LONG, iss_latitude, iss_longitude))
    print(is_currently_dark)
    if is_currently_dark and calculate(MY_LAT, MY_LONG, iss_latitude, iss_longitude):
        send_mail('polepey147@shouxs.com', 'Subject:Notice\n\nLook up')
        print("sent this mail")
    print("wait")
    time.sleep(60)































