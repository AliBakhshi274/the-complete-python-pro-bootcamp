import requests

OWM_Endpoint = 'http://api.openweathermap.org/data/2.5/forecast'
api_key = "15f35a7a376da08080ca75e61c4c60a5"
LON = '35.6944'
LAT = '51.4215'

parameters = {
    'lat': LAT,
    'lon': LON,
    'appid': api_key,
    'cnt': 4,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

for hour_data in weather_data['list']:
    if hour_data['weather'][0]['id'] > 700:
        print("bring your umbrella!")
        break




































