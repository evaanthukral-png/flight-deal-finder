import os
import requests
import requests_cache
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv("SHEETY_USERNAME")
PASSWORD = os.getenv("SHEETY_PASSWORD")

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

class DataManager:
    def __init__(self):
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user,self._password)
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url = SHEETY_ENDPOINT,auth=self._authorization)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        body = {"price": {"lowestPrice": new_price}}
        response = requests.put(url = f"{SHEETY_ENDPOINT}/{row_id}",json = body,auth=self._authorization)
