import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 69
HEIGHT_CM = 179
AGE = 26

APP_ID_EXC =  os.environ.get('APP_ID_EXC')
API_KEY_EXC = os.environ.get('API_KEY_EXC')

exercise_text = input("what did you do today: ")


END_POINT_EXC = os.environ.get('END_POINT_EXC')

headers = {
    "x-app-id": APP_ID_EXC,
    "x-app-key": API_KEY_EXC,
    
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(END_POINT_EXC, json=parameters, headers=headers)
data = response.json()


date = datetime.now().date().strftime("%d/%m/%Y")
time = datetime.now().time().strftime("%X")
for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


url_SHEETY = os.environ.get('url_SHEETY');
AUTHORIZATION = os.environ.get('AUTHORIZATION')

bearer_headers = {
    
    "Authorization": AUTHORIZATION
}




add_to_sheet = requests.post(url_SHEETY, json=sheet_inputs, headers=bearer_headers)
add_response = add_to_sheet.text
print(add_response)