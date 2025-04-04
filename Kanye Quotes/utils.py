import requests

class Kanye:
    def __init__(self):
        pass

    def get_quote(self):
        response = requests.get(url='https://api.kanye.rest')
        if response:
            data = response.json()
            return data['quote']
        else:
            return "Something went wrong"