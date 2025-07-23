#include <iostream>
#include <string>
#include <map>
#include <utility>
#include <iomanip>  // for std::fixed and std::setprecision

using namespace std;

int main() 
{
    int choice;
    string transportType;
    string currentLocation, destination;

    map<pair<string, string>, pair<int, double>> distanceMap = {
        {{"Boston", "New York City"}, {215, 4.0}},
        {{"Boston", "Philadelphia"}, {310, 5.5}},
        {{"Boston", "Cleveland"}, {640, 9.5}},
        {{"Boston", "Baltimore"}, {400, 6.5}},
        {{"Boston", "Washington DC"}, {440, 7.0}},

        {{"New York City", "Boston"}, {215, 4.0}},
        {{"New York City", "Philadelphia"}, {95, 2.0}},
        {{"New York City", "Cleveland"}, {460, 7.5}},
        {{"New York City", "Baltimore"}, {190, 3.5}},
        {{"New York City", "Washington DC"}, {225, 4.0}},

        {{"Philadelphia", "Boston"}, {310, 5.5}},
        {{"Philadelphia", "New York City"}, {95, 2.0}},
        {{"Philadelphia", "Cleveland"}, {430, 6.5}},
        {{"Philadelphia", "Baltimore"}, {100, 2.0}},
        {{"Philadelphia", "Washington DC"}, {140, 2.5}},

        {{"Cleveland", "Boston"}, {640, 9.5}},
        {{"Cleveland", "New York City"}, {460, 7.5}},
        {{"Cleveland", "Philadelphia"}, {430, 6.5}},
        {{"Cleveland", "Baltimore"}, {375, 6.0}},
        {{"Cleveland", "Washington DC"}, {375, 6.0}},

        {{"Baltimore", "Boston"}, {400, 6.5}},
        {{"Baltimore", "New York City"}, {190, 3.5}},
        {{"Baltimore", "Philadelphia"}, {100, 2.0}},
        {{"Baltimore", "Cleveland"}, {375, 6.0}},
        {{"Baltimore", "Washington DC"}, {40, 1.0}},

        {{"Washington DC", "Boston"}, {440, 7.0}},
        {{"Washington DC", "New York City"}, {225, 4.0}},
        {{"Washington DC", "Philadelphia"}, {140, 2.5}},
        {{"Washington DC", "Cleveland"}, {375, 6.0}},
        {{"Washington DC", "Baltimore"}, {40, 1.0}}
    };

    map<pair<string, string>, pair<int, double>> flightMap = {
        // Domestic
        {{"New York City", "Los Angeles"}, {2450, 6.0}},
        {{"New York City", "Austin"}, {1750, 4.0}},
        {{"New York City", "Miami"}, {1280, 3.5}},
        {{"Los Angeles", "Austin"}, {1375, 3.5}},
        {{"Los Angeles", "Miami"}, {2340, 5.5}},
        {{"Austin", "Miami"}, {1100, 3.0}},
        // Reverse domestic
        {{"Los Angeles", "New York City"}, {2450, 6.0}},
        {{"Austin", "New York City"}, {1750, 4.0}},
        {{"Miami", "New York City"}, {1280, 3.5}},
        {{"Austin", "Los Angeles"}, {1375, 3.5}},
        {{"Miami", "Los Angeles"}, {2340, 5.5}},
        {{"Miami", "Austin"}, {1100, 3.0}},
        // International
        {{"New York City", "Tokyo"}, {6750, 14.0}},
        {{"New York City", "London, England"}, {3450, 7.0}},
        {{"New York City", "Paris, France"}, {3625, 7.5}},
        // Return international
        {{"Tokyo", "New York City"}, {6750, 14.0}},
        {{"London, England", "New York City"}, {3450, 7.0}},
        {{"Paris, France", "New York City"}, {3625, 7.5}}
    };

    map<string, pair<int, double>> spaceMap = {
        {"Earth Orbit", {250, 0.5}},       // 0.5 hours
        {"Moon", {238900, 72.0}},          // 72 hours = 3 days
        {"Mars", {140000000, 259200.0}}    // 259200 hours = 10800 days (~30 years approx)
    };

    cout << "What type of transportation do you plan to use?" << endl;
    cout << "1) Land-based travel via car" << endl;
    cout << "2) Airborne travel via plane" << endl;
    cout << "3) Extraterrestrial flight" << endl;
    cout << "Enter your choice (1-3): ";
    cin >> choice;
    cin.ignore();

    switch (choice) {
        case 1:
            transportType = "Land-based travel via car";
            break;
        case 2:
            transportType = "Airborne travel via plane";
            break;
        case 3:
            transportType = "Extraterrestrial flight";
            break;
        default:
            transportType = "Invalid selection";
            break;
    }

    cout << "You selected: " << transportType << endl;

    if (choice >= 1 && choice <= 3) {

        if (choice == 1) {
            cout << "\nNote: Our car-based travel services are currently only available in the Northeast region." << endl;
            cout << "Supported cities: Boston, Cleveland, Philadelphia, New York City, Baltimore, Washington DC." << endl;
        }

        if (choice == 2) {
            cout << "\nNote: Our domestic flights operate between New York City, Los Angeles, Austin, and Miami." << endl;
            cout << "International flights available to Tokyo, London, and Paris." << endl;
        }

        if (choice == 3) {
            cout << "\nNote: Our space travel services currently support:\n";
            cout << " - Earth Orbit (250 miles, ~0.5 hours)\n";
            cout << " - Moon (238,900 miles, ~3 days)\n";
            cout << " - Mars (~140 million miles, ~30 years)\n";
        }

        cout << "\nWhere are you currently located? ";
        getline(cin, currentLocation);

        cout << "Where do you plan to " 
             << (choice == 1 ? "drive" : (choice == 2 ? "fly" : "launch to")) 
             << "? ";
        getline(cin, destination);

        cout << "\nTravel Summary:\n";
        cout << "Transportation: " << transportType << endl;
        cout << "From: " << currentLocation << endl;
        cout << "To: " << destination << endl;

        if (choice == 1) {
            auto route = make_pair(currentLocation, destination);
            if (distanceMap.find(route) != distanceMap.end()) {
                cout << "Estimated Distance: " << distanceMap[route].first << " miles" << endl;
                cout << "Estimated Travel Time: " << distanceMap[route].second << " hours" << endl;
            } else {
                cout << "Sorry, we don't currently support that driving route." << endl;
            }
        }

        if (choice == 2) {
            auto flight = make_pair(currentLocation, destination);
            if (flightMap.find(flight) != flightMap.end()) {
                cout << "Estimated Flight Distance: " << flightMap[flight].first << " miles" << endl;
                cout << "Estimated Flight Time: " << flightMap[flight].second << " hours" << endl;
            } else {
                cout << "Sorry, we don't currently offer flights for that route." << endl;
            }
        }

        if (choice == 3) {
            if (spaceMap.find(destination) != spaceMap.end()) {
                double hours = spaceMap[destination].second;
                double days = hours / 24.0;

                cout << "Estimated Distance to " << destination << ": " << spaceMap[destination].first << " miles" << endl;
                cout << fixed << setprecision(2);
                cout << "Estimated Travel Time: " << days << " days" << endl;
            } else {
                cout << "Sorry, we only support Earth Orbit, Moon, and Mars travel at this time." << endl;
            }
        }

    } else {
        cout << "Unable to proceed with invalid transportation choice." << endl;
    }

    return 0;
}
