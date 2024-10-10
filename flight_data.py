import test_data
class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date,stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops=stops

data=test_data.flight_data

def find_cheapest_flight(data):
    if data is None or not data["data"]:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A",
                          "N/A")
    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin_airport = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination_airport = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    nr_stops=len(first_flight["itineraries"][0]["segments"][0])-1

    cheapest_flight = FlightData(lowest_price, origin_airport, destination_airport, out_date, return_date,nr_stops)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin_airport = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination_airport = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            nr_stops = len(first_flight["itineraries"][0]["segments"][0]) - 1
            cheapest_flight = FlightData(lowest_price, origin_airport, destination_airport, out_date, return_date,nr_stops)
            print(f"lowest flight to destionation{destination_airport} is {lowest_price}")

    return cheapest_flight
