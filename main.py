import requests
from datetime import datetime
import os

GENDER = "Male"
WEIGHT_KG = 160
HEIGHT_CM = 84
AGE = 25

# edit run configuration for environmental variables

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

nutrix = os.environ.get("nutrix")
excel = os.environ.get("excel")
exercise_text = input("Which exercise did you do?: ")
authorization = os.environ.get("authorization")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

sheety_header = {
    "Authorization": authorization,
}

user_parmas = {
    "query": "Running",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutrix_endpoint = f"{nutrix}/v2/natural/exercise"
sheet_endpoint = f"{excel}/workoutSheet/workouts"
##word senstitive workouts worked rather than sheet1

response = requests.post(url=nutrix_endpoint, json=user_parmas, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercise"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

response_00 = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=sheety_header)
result_00 = response_00.json()
