import requests
import os
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

today = datetime.now()
TIME = today.strftime("%X")
DATE = today.strftime("%m/%d/%Y")

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


NUTRIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ["SHEET_ENDPOINT"]

QUERY = input("Tell me which exercises you did: ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": QUERY,
    "weight_kg": YOUR_WEIGHT,
    "height_cm": YOUR_HEIGHT,
    "age": YOUR_AGE
}
response = requests.post(url=NUTRIONIX_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()
exercise_data = data["exercises"][0]

for exercise in data["exercises"]:
    user_params = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        url=SHEETY_ENDPOINT,
        json=user_params,
        auth=(USERNAME, PASSWORD)
    )

    print(sheet_response.text)

