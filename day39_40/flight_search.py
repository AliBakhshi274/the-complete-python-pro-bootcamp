import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.ENDPOINT = "https://test.api.amadeus.com"
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url = f"{self.ENDPOINT}/v1/security/oauth2/token",headers=headers, data=body)
        response.raise_for_status()
        return response.json()['access_token']

    def get_city_code(self, city_name):
        headers = {
            "accept": "application/vnd.amadeus+json",
            "Authorization": f"Bearer {self._token}",
        }
        query = {
            "subType": "AIRPORT",
            "keyword": city_name,
        }
        response = requests.get(url = f"{self.ENDPOINT}/v1/reference-data/locations", headers=headers, params=query)
        try:
            destination_code = response.json()["data"][0]["address"]["cityCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}")
            return "Not Found"
        return destination_code

    def check_flights(self, origin_city, destination_city, from_date, to_date, is_direct=False):
        headers = {
            'Authorization': f"Bearer {self._token}",
        }
        query = {
            "originLocationCode": origin_city,
            "destinationLocationCode": destination_city,
            "departureDate": from_date,
            "returnDate": to_date,
            "adults": 1,
            'max': 10,
            'currencyCode': 'GBP',
            'nonStop': str(is_direct).lower(),
        }
        response = requests.get(url = f"{self.ENDPOINT}/v2/shopping/flight-offers", headers=headers, params=query)
        return response.json()























