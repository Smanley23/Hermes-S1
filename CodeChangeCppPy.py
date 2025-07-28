def main():
    distance_map = {
        ("Boston", "New York City"): (215, 4.0),
        ("Boston", "Philadelphia"): (310, 5.5),
        ("Boston", "Cleveland"): (640, 9.5),
        ("Boston", "Baltimore"): (400, 6.5),
        ("Boston", "Washington DC"): (440, 7.0),

        ("New York City", "Boston"): (215, 4.0),
        ("New York City", "Philadelphia"): (95, 2.0),
        ("New York City", "Cleveland"): (460, 7.5),
        ("New York City", "Baltimore"): (190, 3.5),
        ("New York City", "Washington DC"): (225, 4.0),

        ("Philadelphia", "Boston"): (310, 5.5),
        ("Philadelphia", "New York City"): (95, 2.0),
        ("Philadelphia", "Cleveland"): (430, 6.5),
        ("Philadelphia", "Baltimore"): (100, 2.0),
        ("Philadelphia", "Washington DC"): (140, 2.5),

        ("Cleveland", "Boston"): (640, 9.5),
        ("Cleveland", "New York City"): (460, 7.5),
        ("Cleveland", "Philadelphia"): (430, 6.5),
        ("Cleveland", "Baltimore"): (375, 6.0),
        ("Cleveland", "Washington DC"): (375, 6.0),

        ("Baltimore", "Boston"): (400, 6.5),
        ("Baltimore", "New York City"): (190, 3.5),
        ("Baltimore", "Philadelphia"): (100, 2.0),
        ("Baltimore", "Cleveland"): (375, 6.0),
        ("Baltimore", "Washington DC"): (40, 1.0),

        ("Washington DC", "Boston"): (440, 7.0),
        ("Washington DC", "New York City"): (225, 4.0),
        ("Washington DC", "Philadelphia"): (140, 2.5),
        ("Washington DC", "Cleveland"): (375, 6.0),
        ("Washington DC", "Baltimore"): (40, 1.0)
    }

    flight_map = {
        ("New York City", "Los Angeles"): (2450, 6.0),
        ("New York City", "Austin"): (1750, 4.0),
        ("New York City", "Miami"): (1280, 3.5),
        ("Los Angeles", "Austin"): (1375, 3.5),
        ("Los Angeles", "Miami"): (2340, 5.5),
        ("Austin", "Miami"): (1100, 3.0),

        ("Los Angeles", "New York City"): (2450, 6.0),
        ("Austin", "New York City"): (1750, 4.0),
        ("Miami", "New York City"): (1280, 3.5),
        ("Austin", "Los Angeles"): (1375, 3.5),
        ("Miami", "Los Angeles"): (2340, 5.5),
        ("Miami", "Austin"): (1100, 3.0),

        ("New York City", "Tokyo"): (6750, 14.0),
        ("New York City", "London, England"): (3450, 7.0),
        ("New York City", "Paris, France"): (3625, 7.5),

        ("Tokyo", "New York City"): (6750, 14.0),
        ("London, England", "New York City"): (3450, 7.0),
        ("Paris, France", "New York City"): (3625, 7.5)
    }

    space_map = {
        "Earth Orbit": (250, 0.5),
        "Moon": (238900, 72.0),
        "Mars": (140000000, 259200.0)
    }

    print("What type of transportation do you plan to use?")
    print("1) Land-based travel via car")
    print("2) Airborne travel via plane")
    print("3) Extraterrestrial flight")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        transport_type = "Land-based travel via car"
    elif choice == '2':
        transport_type = "Airborne travel via plane"
    elif choice == '3':
        transport_type = "Extraterrestrial flight"
    else:
        transport_type = "Invalid selection"

    print(f"You selected: {transport_type}")

    if choice in ['1', '2', '3']:
        if choice == '1':
            print("\nNote: Our car-based travel services are currently only available in the Northeast region.")
            print("Supported cities: Boston, Cleveland, Philadelphia, New York City, Baltimore, Washington DC.")
        elif choice == '2':
            print("\nNote: Our domestic flights operate between New York City, Los Angeles, Austin, and Miami.")
            print("International flights available to Tokyo, London, and Paris.")
        elif choice == '3':
            print("\nNote: Our space travel services currently support:")
            print(" - Earth Orbit (250 miles, ~0.5 hours)")
            print(" - Moon (238,900 miles, ~3 days)")
            print(" - Mars (~140 million miles, ~30 years)")

        current_location = input("\nWhere are you currently located? ")
        destination = input("Where do you plan to " + ("drive" if choice == '1' else "fly" if choice == '2' else "launch to") + "? ")

        print("\nTravel Summary:")
        print(f"Transportation: {transport_type}")
        print(f"From: {current_location}")
        print(f"To: {destination}")

        if choice == '1':
            route = (current_location, destination)
            if route in distance_map:
                dist, time = distance_map[route]
                print(f"Estimated Distance: {dist} miles")
                print(f"Estimated Travel Time: {time:.1f} hours")
            else:
                print("Sorry, we don't currently support that driving route.")
        elif choice == '2':
            route = (current_location, destination)
            if route in flight_map:
                dist, time = flight_map[route]
                print(f"Estimated Flight Distance: {dist} miles")
                print(f"Estimated Flight Time: {time:.1f} hours")
            else:
                print("Sorry, we don't currently offer flights for that route.")
        elif choice == '3':
            if destination in space_map:
                dist, time_hours = space_map[destination]
                time_days = time_hours / 24.0
                print(f"Estimated Distance to {destination}: {dist:,} miles")
                print(f"Estimated Travel Time: {time_days:.2f} days")
            else:
                print("Sorry, we only support Earth Orbit, Moon, and Mars travel at this time.")
    else:
        print("Unable to proceed with invalid transportation choice.")

if __name__ == "__main__":
    main()
