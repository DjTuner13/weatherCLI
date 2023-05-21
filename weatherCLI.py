#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "David Ranoia"
__version__ = "0.1.0"
__license__ = "MIT"

#imports

import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Access the environment variables
API = os.getenv("API")

#variables
city = "stratford"
state = "NJ"
country = "US"
limit = 100
zipcode = "08084"
lat = "39.8288"
lon = "-75.0147"


def main():
    print("hello world")
    responseLocation = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state}&limit=5&appid={API}")

    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={API}")

    geoLocationByZip = requests.get(f"http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{country}&appid={API}")

    forcast = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API}")

    #print(responseLocation.text)
    #print(response.text)
    #print(geoLocationByZip.text)
    #print(forcast.text)

    # Get the JSON content from the response
    data = forcast.json()
    """
    # Specify the output file path
    output_file_path = "outputForcast.json"

    # Write the JSON data to the file
    with open(output_file_path, "w") as file:
        json.dump(data, file, indent=4)

    # Read JSON data from file
    with open("outputForcast.json") as file:
        data = json.load(file)

    # Access and print the "description" field
    description = data["list"][0]["weather"][0]["description"]
    print("Description:", description)
    """
    # Access and print the "description" field
    description = data["list"][0]["weather"][0]["description"]
    print("Description:", description)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
