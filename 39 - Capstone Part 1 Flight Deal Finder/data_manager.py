import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/*************************/flightDeals/prices/"

class DataManager:

    def __init__(self):
        self.destinantion_data = {}
    
    def get_destinantion_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destinantion_data = data["prices"]
        return self.destinantion_data
    
    def update_destiantion_codes(self):
        for city in self.destinantion_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
        response = requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
            json = new_data
        )
        print(response.text)