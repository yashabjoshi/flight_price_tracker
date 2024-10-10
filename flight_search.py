import requests
# from datetime import datetime


IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
AUTHOR_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
SEARCH_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:
    def __init__(self):
        self.token_code = self.get_token()
        self.header = {
            "Authorization": f"Bearer {self.token_code}"
        }

    def get_token(self):
        token_auth = {"grant_type": "client_credentials",
                      "client_id": "0e9J0Fgdk31wwb9GTixNnkGaYl1VGBZ0",
                      "client_secret": "1jnvZzPwLAJbsjag"
                      }
        token_response = requests.post(AUTHOR_ENDPOINT, data=token_auth)
        token_response.raise_for_status()
        access_token = token_response.json()["access_token"]
        return access_token

    def get_iata_code(self, city_name):
        self.iata_config = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=IATA_ENDPOINT, params=self.iata_config, headers=self.header)
        print(f"status code:{response.status_code}, Airport IATA:{response.text}")

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def check_flight(self, departure_code, destination_code, from_date, to_date,is_direct=True):

        self.search_config = {
            "originLocationCode": departure_code,
            "destinationLocationCode": destination_code,
            "departureDate": from_date.strftime("%Y-%m-%d"),
            "returnDate": to_date.strftime("%Y-%m-%d"),
            "nonStop": "true" if is_direct else "false",
            "adults": 1,
            "currencyCode": "GBP",
            "max": "10",
        }
        response = requests.get(url=SEARCH_ENDPOINT, params=self.search_config, headers=self.header)
        if response.status_code != 200:
            print(f"check_flight() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
