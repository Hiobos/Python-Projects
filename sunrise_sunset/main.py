import requests
from datetime import datetime

MY_LAT = 54.352024
MY_LONG = 18.646639

parameters = {
    "lat": MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
    'tzid': 'Europe/Warsaw'
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
print(response.json())
response = response.json()
sunrise = response['results']['sunrise'].split('T')[1].split(':')[0]
sunset = response['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)