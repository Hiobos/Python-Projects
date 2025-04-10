import requests
from datetime import datetime

from sunrise_sunset.main import response

pixela_endpoint = 'https://pixe.la/v1/users'

TOKEN = open('key/token.txt', 'r').read()
USERNAME = 'user1schnoz'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_id = 'graph1'

graph_param = {
    'id': graph_id,
    'name': 'reading graph',
    'unit': 'pages',
    'type': 'int',
    'color': 'momiji'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_param, headers=headers)
# print(response.text)

pixel_add_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"

date = datetime.now().strftime("%Y%m%d")

pixel_add_params = {
    'date': date,
    'quantity': '20'
}


# response = requests.post(url=pixel_add_endpoint, json=pixel_add_params, headers=headers)
# print(response.text)

pixel_update = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{date}"

update = {
    'quantity': '50'
}

response1 = requests.delete(url=pixel_update, json=update, headers=headers)
print(response1.text)
