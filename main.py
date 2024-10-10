# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time

from data_manager import Datamanger, get_email
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
import smtplib
MY_EMAIL ="abc@gmail.com"
MY_PASSWORD = "acjsjdk"
DEPARTURE_CODE = "LON"

datasheet = Datamanger()
flight_search = FlightSearch()

#get data from datasheet
code_data = datasheet.get_data()

# update data
if code_data[0]["iataCode"] == "":
    for row in code_data:
        row["iataCode"] = flight_search.get_iata_code(row["city"])
        time.sleep(2)
    datasheet.destination_data = code_data
    datasheet.update_destination_code()
#check flights
tomorrow = datetime.today() + timedelta(days=1)
six_months = datetime.today() + timedelta(days=6 * 30)
for row in code_data:
    flights = flight_search.check_flight(DEPARTURE_CODE, row["iataCode"], tomorrow, six_months,is_direct=True)
    if all(data=="N/A" for data in flights) and flights.is_direct=="true":
        flights = flight_search.check_flight(DEPARTURE_CODE, row["iataCode"], tomorrow, six_months, is_direct=False)
    time.sleep(2)
    cheapest_flight = find_cheapest_flight(flights)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < row["lowestPrice"]:
        body = (f"low price alreat! only ${cheapest_flight.price} to fly from{DEPARTURE_CODE} to "
                f"{cheapest_flight.destination_airport},on {cheapest_flight.out_date}  until"
                f" {cheapest_flight.return_date} stops:{cheapest_flight.stops}")
        email_list=get_email()
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for users in email_list:
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=users,
                                    msg=f"Subject:Price alert!\n\n {body}"
                                    )

