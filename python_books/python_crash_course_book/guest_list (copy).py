#!/usr/bin/env python3
from typing import Dict, Union


def main():
    # a simple dictionary
    alien_0 = {"color": "green", "points": 5}
    print(alien_0["color"])
    print(alien_0["points"])
    new_points = alien_0["points"]
    print(f"You just earned {new_points} points!")

    # to add a new key-value pair
    alien_0["x_position"] = 0
    alien_0["y_position"] = 25
    print(alien_0)

    # modifying the values in a dict
    print(f'The alien is {alien_0["color"]}')
    alien_0["color"] = "yellow"
    print(f'The alien is now {alien_0["color"]}')

    # removing key-value pairs
    del alien_0["points"]

    # to avoid an error when the key doesn't exist
    point_value = alien_0.get("points", "No points value assigned.")
    print(point_value)

    # looping through a dictionary
    polina_feat = {}
    polina_feat["first_name"] = "Polina"
    polina_feat["last_name"] = "Uluanova"
    polina_feat["Age"] = 21
    polina_feat["city"] = "SPB"
    for key, value in polina_feat.items():
        print(f"{key} - {value}")

    # looping through all keys in a dictionary
    for features in polina_feat.keys():
        print(features.upper())
    print()
    friends = ["Max", "Stan"]
    favorite_language = {"Max": "C", "Stan": "Python"}
    for friend in friends:
        print(f"{friend} likes {favorite_language[friend]}")

    # looping through a dictionary's keys in a particular order(sorted or sort function)
    for feat in sorted(polina_feat.keys(), reverse=True):
        print(f"{feat}")


if __name__ == "__main__":
    main()
