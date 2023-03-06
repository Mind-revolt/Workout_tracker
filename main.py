import json
import requests
import os
import datetime as dt
from requests.auth import HTTPBasicAuth

APP_ID_NUTRI = os.environ.get("API_ID_NUTRI")
NUTRI_URL = os.environ.get("NUTRI_URL")
API_KEY_NUTRI = os.environ.get("API_KEY_NUTRI")

USERNAME = os.environ.get("SHEETY_USERNAME")
PASSWORD = os.environ.get("NUTRI_PASS")
SHEETY_URL = os.environ.get("SHEETY_URL")
SHEETY_AUTH = os.environ.get("SHEETY_BASIC_AUTH")
EMAIL = os.environ.get("EMAIL")
AUTH_USER = os.environ.get("AUTH_USERNAME")
AUTH_PASS = os.environ.get("AUTH_PASS")
http_auth = HTTPBasicAuth(username=f'{AUTH_USER}', password=f'{AUTH_PASS}')
now = dt.datetime.now()
today = now.date()
now_time = now.strftime("%H:%M:%S")

# log into Nutritionix
headers = {
    "x-app-id": APP_ID_NUTRI,
    "x-app-key": API_KEY_NUTRI,
    "Authorization": f"{SHEETY_AUTH}",
    "Content-Type": "application/json",
    "x-remote-user-id": "0",
}
# post query
query_post_body = {
     "query": f"{input('What workouts did you do today? ')}",
     "gender": "male",
     "weight_kg": 68,
     "height_cm": 182,
     "age": 26
}
nutri_post = requests.post(url=NUTRI_URL, json=query_post_body, headers=headers)
raw_response = json.loads(nutri_post.text)
exercise = raw_response["exercises"][0]["name"]
duration = raw_response["exercises"][0]["duration_min"]
burned_calories = raw_response["exercises"][0]["nf_calories"]

sheety_body = {
    "workout": {
        "exercise": f"{exercise}",
        "date": str(today),
        "time": str(now_time),
        "duration": f"{duration} min",
        "calories": str(burned_calories)
    }
}

# user credentials
user = {
    "password": f"{PASSWORD}",
    "email": f"{EMAIL}",
}
# access rows
access_rows = requests.get(url=SHEETY_URL, headers=headers, auth=http_auth)
# # add new rows
# print(raw_response)
add_row = requests.post(url=SHEETY_URL, headers=headers, json=sheety_body)
print(add_row.text)
print(access_rows.text)


