import requests
import datetime as dt
import dotenv
import os

dotenv.load_dotenv()                    
ex_app_id = os.environ.get("ex_app_id")
ex_api_key = os.environ.get("ex_api_key")
sh_api = os.environ.get("sh_api")
Authorization = os.environ.get("Authorization")

host_endpoint="https://trackapi.nutritionix.com"
exercise_endpoint=f"{host_endpoint}//v2/natural/exercise"
today = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%H:%M:%S")

headers={
    "Content-Type":"application/json",
    "x-app-id":ex_app_id,
    "x-app-key":ex_api_key,
}



ex_params={
    "query": input("What did you do for excersice?")
}


res = requests.post(url=exercise_endpoint, headers=headers, json=ex_params)
data = res.json()
print(data)
exercise = data["exercises"][0]["name"].capitalize()
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]


sh_params={
    "シート1": {
        "date":today,
        "time":time,
        "exercise":exercise,
        "duration":duration,
        "calories":calories
    }
}

headers={
    "Authorization":Authorization
}

res = requests.post(url=sh_api, json=sh_params, headers=headers)
data = res.json()
print(data)