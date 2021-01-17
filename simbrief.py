import requests
import json

FETCH_URL = "http://www.simbrief.com/api/xml.fetcher.php?json=1&username="
DISPATCH_URL = "http://www.simbrief.com/system/dispatch.php?"


class InvalidArgumentException(Exception):
    # Custom Exception Class
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def fetch(SIMBRIEF_USERNAME):
    # Fetches some basic information from your latest simbrief flight plan.
    url = FETCH_URL + SIMBRIEF_USERNAME
    url_data = requests.get(url).content
    parsed = json.loads(url_data)

    print("~~ Basic Information ~~")
    print("Origin: {} ({})".format(
        parsed["origin"]["icao_code"], parsed["origin"]["iata_code"]))
    print("Planned Runway: {}".format(parsed["origin"]["plan_rwy"]))
    print("Destination: {} ({})".format(
        parsed["destination"]["icao_code"], parsed["destination"]["iata_code"]))
    print("Planned Runway: {}".format(parsed["destination"]["plan_rwy"]))
    print("Alternate: {} ({})".format(
        parsed["alternate"]["icao_code"], parsed["alternate"]["iata_code"]))
    print("\n~~ Route Information ~~")
    print("Route: {}".format(parsed["general"]["route"]))
    print("Planned Altitude: {}".format(parsed["general"]["initial_altitude"]))
    print("\n~~ Weight & Balance ~~")
    print("Fuel: {}".format(parsed["fuel"]["plan_ramp"]))
    print("Zero Fuel Weight: {}".format(parsed["weights"]["est_zfw"]))
    print("\n~~ Weather Information ~~")
    print("Weather Origin:\n{}".format(parsed["weather"]["orig_metar"]))
    print("Weather Destination:\n{}".format(parsed["weather"]["dest_metar"]))
    print("Weather Alternate:\n{}".format(parsed["weather"]["altn_metar"]))


if __name__ == "__main__":
    fetch(input("Enter simbrief username: "))
