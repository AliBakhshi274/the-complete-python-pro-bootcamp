import requests
import datetime as dt
import os

def get_exercises_details():
    host_end_point = "https://trackapi.nutritionix.com"
    exercise_end_point = "v2/natural/exercise"

    APP_ID = os.environ["APP_ID"]
    APP_KEY = os.environ["APP_KEY"]

    user_exercise = input("Tell me which exercises you did: ")

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
        "x-remote-user-id": "0",
    }
    parameters = {
        "query": user_exercise,
    }

    response = requests.post(f"{host_end_point}/{exercise_end_point}", headers=headers, json=parameters)
    exercises_list = response.json().get("exercises")
    ex_duration_minutes_list = []
    ex_name_list = []
    ex_nf_calories_list = []
    for exercise in exercises_list:
        ex_name_list.append(exercise.get("name"))
        ex_duration_minutes_list.append(exercise.get("duration_min"))
        ex_nf_calories_list.append(exercise.get("nf_calories"))
    return ex_name_list, ex_duration_minutes_list, ex_nf_calories_list

def post_data_using_sheety(exercise_names, exercise_durations, exercise_calories):
    project_name = "workoutTracking"
    SHEET_USERNAME = os.environ["SHEET_USERNAME"]
    SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]
    sheet_endpoint = f"https://api.sheety.co/{SHEET_USERNAME}/{project_name}/workouts"
    workouts = []
    for i in range(0, len(exercise_names)):
        workouts.append({
            "date": dt.datetime.today().strftime("%d/%m/%Y"),
            "time": dt.datetime.today().strftime("%H:%M:%S"),
            "exercise": exercise_names[i],
            "duration": exercise_durations[i],
            "calories": exercise_calories[i],
        })
    headers = {
        "Authorization": SHEETY_PASSWORD,
        "Content-Type": "application/json",
    }
    for workout in workouts:
        parameters = {"workout": workout}
        response = requests.post(url=sheet_endpoint,headers=headers, json=parameters)
        print(response.json())

name_list, duration_list, calories_list = get_exercises_details()
post_data_using_sheety(name_list, duration_list, calories_list)






















