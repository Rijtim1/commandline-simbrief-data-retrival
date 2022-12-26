import requests
import json

def fetch_flight_plan(simbrief_username):
    api_url = "http://www.simbrief.com/api/xml.fetcher.php"
    params = {"json": 1, "username": simbrief_username}
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    return response.json()

def print_flight_plan_info(flight_plan):
    origin = flight_plan["origin"]
    destination = flight_plan["destination"]
    alternate = flight_plan["alternate"]
    general = flight_plan["general"]
    fuel = flight_plan["fuel"]
    weights = flight_plan["weights"]
    weather = flight_plan["weather"]

    print("~~ Basic Information ~~")
    print(f"Origin: {origin['icao_code']} ({origin['iata_code']})")
    print(f"Planned Runway: {origin['plan_rwy']}")
    print(f"Destination: {destination['icao_code']} ({destination['iata_code']})")
    print(f"Planned Runway: {destination['plan_rwy']}")
    print(f"Alternate: {alternate['icao_code']} ({alternate['iata_code']})")
    print("\n~~ Route Information ~~")
    print(f"Route: {general['route']}")
    print(f"Planned Altitude: {general['initial_altitude']}")
    print("\n~~ Weight & Balance ~~")
    print(f"Fuel: {fuel['plan_ramp']}")
    print(f"Payload: {weights['payload']}")
    print("\n~~ Weather Information ~~")
    print(f"Weather Origin:\n{weather['orig_metar']}")
    print(f"Weather Destination:\n{weather['dest_metar']}")
    print(f"Weather Alternate:\n{weather['altn_metar']}")

def main():
    try:
        with open("username.txt", "r") as username_file:
            simbrief_username = username_file.readline().strip()
    except IOError:
        with open("username.txt", "w") as username_file:
            simbrief_username = input("Enter simbrief name: ").strip()
            username_file.write(simbrief_username)
    flight_plan = fetch_flight_plan(simbrief_username)
    print_flight_plan_info(flight_plan)

if __name__ == "__main__":
    main()
