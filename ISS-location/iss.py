import requests
from NightOrDay import TimeOfDay
daytime = TimeOfDay()

class ISS:
    def __init__(self):
        pass

    def location(self, my_lat, my_lng):
        response_iss = requests.get('http://api.open-notify.org/iss-now.json')
        data_iss = response_iss.json()
        iss_lng = float(data_iss['iss_position']['longitude'])
        iss_lat = float(data_iss['iss_position']['latitude'])

        lng_range = (my_lng - 5, my_lng + 5)
        lat_range = (my_lat - 5, my_lat + 5)

        actual_time = daytime.daytime(my_lat, my_lng)

        if lng_range[0] <= iss_lng <= lng_range[1] and lat_range[0] <= iss_lat <= lat_range[1]:
            if actual_time == 'Night':
                print("It's above")
            else:
                print("ISS is above but not visible during day.")
        else:
            print(f"It's not above right now, current longitude: {iss_lng}, latitude: {iss_lat}")