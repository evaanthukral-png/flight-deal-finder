from data_manager import DataManager
from pprint import pprint
import requests_cache
from datetime import datetime,timedelta
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

notification_manager = NotificationManager()

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

# ==================== Talk to Sheety ====================

data_manager = DataManager()
sheet_data = data_manager.get_data()
# pprint(sheet_data)

# ==================== Set the Dates ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# ==================== Do a Flight Search ====================

flight_search = FlightSearch()
for destinations in sheet_data:
    flights = flight_search.check_flights(
        origin_city_code="LHR",
        destination_city_code=destinations['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today
    )



    cheapest_flight = FlightData.find_cheapest_flight(
        flights,
        return_date=six_month_from_today.strftime("%Y-%m-%d")
    )
    pprint(f"{destinations['city']}: USD {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destinations["lowestPrice"]:
        print("Inside if block")
        print(f"Lower price flight found to {destinations['city']}!")

        data_manager.update_lowest_price(
            destinations["id"],
            cheapest_flight.price
        )

        message = (
            f"Low price alert!\n"
            f"Only GBP {cheapest_flight.price} to fly "
            f"from {cheapest_flight.origin_airport} "
            f"to {cheapest_flight.destination_airport}.\n"
            f"Out: {cheapest_flight.out_date}\n"
            f"Return: {cheapest_flight.return_date}"
        )

        notification_manager.send_sms(message)
#
# print("Flight price:", cheapest_flight.price)
# print("Sheet price:", destinations["lowestPrice"])
# print("Price is N/A?", cheapest_flight.price == "N/A")
# print("Is cheaper?", cheapest_flight.price < destinations["lowestPrice"])