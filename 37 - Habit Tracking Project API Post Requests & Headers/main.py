import requests
from datetime import datetime

USERNAME = "YOR USERNAME"
TOKEN = "YOUR SELF GENERATED TOKEN"
GRAPH_ID = "YOUR GRAPH ID"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Study Graph",
    "unit": "Hour",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(reponse.text)

pixel_creation_endpoint = f"{pixela_endpoint} / {USERNAME} / graphs / {{GRAPH_ID}}"

today = datetime.now()
#print(today.strftime("%Y%m%d"))

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today?"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint} / {USERNAME} / graphs / {GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quatity": "5"
}

#PUT
# response = requests.post(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(reponse.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graph/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)