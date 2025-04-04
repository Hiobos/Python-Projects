import requests
from datetime import datetime

class TimeOfDay:
    def __init__(self):
        self.parameters = {
            "lat": '',
            'lng': '',
            'formatted': 0,
            'tzid': 'Europe/Warsaw'
        }

    def daytime(self, my_lat, my_lng):
        self.parameters['lat'] = my_lat
        self.parameters['lng'] = my_lng

        response = requests.get('https://api.sunrise-sunset.org/json', params=self.parameters)
        response = response.json()
        sunrise = response['results']['sunrise'].split('T')[1].split(':')[0]
        sunset = response['results']['sunset'].split('T')[1].split(':')[0]
        time_now = datetime.now()

        if int(time_now.hour) > int(sunset):
            return "Night"
        else:
            return "Day"