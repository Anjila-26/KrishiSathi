import time
import requests
import firebase_admin
from firebase_admin import credentials, db
import json
from datetime import datetime


# Fetch the service account key JSON file path
cred = credentials.Certificate("xada-gai-firebase.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(
    cred,
    {"databaseURL": "https://xada-gai-default-rtdb.firebaseio.com"},
)

CLASS_MAPPING = {
    1: "cow",
    2: "dog",
    3: "tiger",
    4: "elephant",
}


def call_after_interval(interval_seconds):
    def decorator(func):
        last_called = 0

        def wrapper(*args, **kwargs):
            nonlocal last_called
            current_time = time.time()
            if current_time - last_called >= interval_seconds:
                last_called = current_time
                return func(*args, **kwargs)

        return wrapper

    return decorator


@call_after_interval(300)  # Function can only be called after 5 seconds
def sendMessage():

    classes, lat, long, time = load_data()
    message = ""
    # classes = data["classes"]
    # time = data["time"]
    if len(data["classes"]) == 1:
        message = f"Alert!! {classes} was detected at lat:{lat}, long:{long}, {time}"
    else:
        message = f"Alert!! {classes} were detected at lat:{lat}, long:{long}, {time}"

    with open(
        "C:\\Users\\siddh\\OneDrive\\Desktop\\datacrunch2024\\test\\The-Kripples\\ml-backend\\smsCred.json",
        "r",
    ) as file:
        data = json.load(file)

    re = requests.post(
        "https://sms.aakashsms.com/sms/v3/send/",
        data={
            "auth_token": data["auth_token"],
            "to": data["phones"],
            "text": message,
        },
    )


@call_after_interval(300)  # Function can only be called after 5 seconds
def save_to_firebase(classes):
    # Get a database reference to the root node
    ref = db.reference("/")

    # Get the current time
    current_date = datetime.now().date()
    current_time = datetime.now().replace(microsecond=0).time()
    current = str(current_date) + " " + str(current_time)

    # Convert int64 values to regular Python integers
    classes = [int(c) for c in classes]

    # Push detected classes and time to the database
    ref.push(
        {"classes": classes, "time": current_time, "lat": 27.638728, "long": 85.334618}
    )


def get_all_data():
    ref = db.reference("/")
    all_data = ref.get()
    return all_data


def load_data():
    all_data = get_all_data()
    list_of_classes = []

    if all_data is None:
        print("No data found in the database.")
    else:
        for key, data in all_data.items():
            time = data["time"]
            classes = data["classes"]
            lat = data["lat"]
            long = data["long"]
            for i in range(len(classes)):
                classes[i] = CLASS_MAPPING[classes[i]]
            list_of_classes.append(data)
    return list_of_classes[-1], lat, long, time
