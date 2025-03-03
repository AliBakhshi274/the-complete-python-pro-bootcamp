#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
import flight_search
import datetime as dt
from flight_data import find_cheapest_flight
import notification_manager

ORIGIN_CITY_IATA = 'LON'

data_manager = data_manager.DataManager()
flight_search = flight_search.FlightSearch()
notification_manager = notification_manager.NotificationManager()

sheet_data_users: list = data_manager.get_customer_infos()
sheet_data_prices : list = data_manager.get_sheet_prices()

# Fill the IATACODE column
for row in sheet_data_prices:
    if row['iataCode'] == "" :
        destination_code = flight_search.get_city_code(row['city'])
        row['iataCode'] = destination_code
        data_manager.update_entry(row)

tomorrow = str(dt.datetime.now() + dt.timedelta(days=1)).split(' ')[0]
six_month_later = str(dt.datetime.now() + dt.timedelta(days=6 * 30)).split(' ')[0]

for row in sheet_data_prices:
    flights = flight_search.check_flights(ORIGIN_CITY_IATA, row['iataCode'], tomorrow, six_month_later)
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{row['city']} -> {cheapest_flight.price}$ / from: {cheapest_flight.origin_airport} / to: {cheapest_flight.destination_airport}")
    if cheapest_flight.price == "N/A":
        # print(f"No direct flight to {row['city']}....")
        stopover_flights = flight_search.check_flights(ORIGIN_CITY_IATA, row['iataCode'], tomorrow, six_month_later, is_direct= False)
        cheapest_flight = find_cheapest_flight(stopover_flights)
        # print(f"{row['city']} -> {cheapest_flight.price}$ / from: {cheapest_flight.origin_airport} / to: {cheapest_flight.destination_airport}")
        # print("has a flight?")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < row['lowestPrice']:
        message = (f"cheapest price from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}"
                   f" with {cheapest_flight.price}$ at {cheapest_flight.out_date} and return date is {cheapest_flight.return_date} ")
        notification_manager.send_mail(recipients_data = sheet_data_users, message=message)
































