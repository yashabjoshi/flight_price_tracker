
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/dae26e63ae929f7c0580638c26d6642e/flightDeals/prices"
SHEETY_AUTHOR = {"Authorization": "Basic ZmxpZ2h0czpkZWRlZGVkbHBscA=="}
EMAIL_ENDPOINT="https://api.sheety.co/dae26e63ae929f7c0580638c26d6642e/flightUsersData/formResponses1"

class Datamanger:
    def __init__(self):
        self.destination_data = {}


    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_AUTHOR)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {"iataCode": city['iataCode']}
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data, headers=SHEETY_AUTHOR)


def get_email():
    response = requests.get(url=EMAIL_ENDPOINT)
    data = response.json()["formResponses1"]
    email_list=[]
    for row in data:
        email_list.append(row["whatIsYourEmailId?"])

    return email_list
list=get_email()
