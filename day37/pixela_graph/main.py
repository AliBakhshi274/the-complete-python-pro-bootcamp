import requests
import datetime as dt

end_point = "https://pixe.la/v1/users"
username = "ahmadreza"
TOKEN = "alibakhshi274"
graph_id = "ask456"
def create_user():
    parameters = {
        "token": TOKEN,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    requests.post(end_point, json=parameters)

def create_graph():
    parameters = {
        "id": graph_id,
        "name": "myGraph",
        "unit": "hours",
        "type": "float",
        "color": "shibafu",
    }
    headers = {
        "X-USER-TOKEN": TOKEN,
    }
    requests.post(f"{end_point}/{username}/graphs", json=parameters, headers=headers)

def post_pixel():
    today = dt.datetime.today()
    headers = {
        "X-USER-TOKEN": TOKEN,
    }
    parameters = {
        "date": str(today.strftime("%Y%m%d")),
        "quantity": "15",
    }
    response = requests.post(f"{end_point}/{username}/graphs/{graph_id}", json=parameters, headers=headers)

def update_pixel():
    headers = {
        "X-USER-TOKEN": TOKEN,
    }
    parameters = {
        "color": "ichou",
        "unit": "kilogram",
        "timezone": "Asia/Tehran",
    }
    response = requests.put(f"{end_point}/{username}/graphs/{graph_id}", json=parameters, headers=headers)
    print(response.json())

# create_user()
# create_graph()
# post_pixel()
update_pixel()






















