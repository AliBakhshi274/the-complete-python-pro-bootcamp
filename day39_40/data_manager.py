import os
from dotenv import load_dotenv
import requests

load_dotenv()

SHEETY_API_URL = "https://api.sheety.co"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_TOKEN"]
        self.sheety_url_prices = f"{SHEETY_API_URL}/{self._user}/flightDeals/prices"
        self.sheety_url_users = f"{SHEETY_API_URL}/{self._user}/flightDeals/users"
        self.headers = {
            "Authorization": self._password,
            "Content-Type": "application/json",
        }

    def get_sheet_prices(self) -> list:
        response = requests.get(url=self.sheety_url_prices, headers=self.headers)
        response.raise_for_status()
        return response.json()["prices"]

    def get_customer_infos(self) -> list:
        response = requests.get(url=self.sheety_url_users, headers=self.headers)
        response.raise_for_status()
        return response.json()["users"]

    def update_entry(self, entry):
        put_url = f"{self.sheety_url_prices}/{entry['id']}"
        body = {
            "price": {
                "iataCode": entry["iataCode"]
            }
        }
        response = requests.put(url=put_url, headers=self.headers, json=body)
        response.raise_for_status()

























