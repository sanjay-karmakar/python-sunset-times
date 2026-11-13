# pip install requests

import datetime as dt
import requests
import os
from dotenv import load_dotenv

# Load variables from the .env file into your environment
load_dotenv()
MY_LAT=os.environ.get("MY_LAT")
MY_LANG=os.environ.get("MY_LANG")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LANG,
    "formatted": 0
}

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset  = data['results']['sunset'].split("T")[1].split(":")[0]

time_now = dt.datetime.now()

print(f"Sunrise time: {sunrise}hr")
print(f"Sunset time: {sunset}hr")

# print(time_now.hour, sunrise, sunset)
