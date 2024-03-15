import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Mapping of class IDs to their names
CLASS_MAPPING = {1: "cow", 2: "dog", 3: "tiger", 4: "elephant"}


class FirebaseDB:
    def __init__(self, service_account_key_path, database_url):
        self.service_account_key_path = service_account_key_path
        self.database_url = database_url
        self._initialize_firebase()

    def _initialize_firebase(self):
        cred = credentials.Certificate(self.service_account_key_path)
        firebase_admin.initialize_app(cred, {"databaseURL": self.database_url})

    def get_most_recent_data(self):
        ref = db.reference("/")
        query = ref.order_by_child("time").limit_to_last(1)
        most_recent_data = query.get()
        return most_recent_data


if __name__ == "__main__":
    # Initialize FirebaseDB object
    firebase_db = FirebaseDB(
        "xada-gai-firebase-adminsdk-oyyho-4c1f80d772.json",
        "https://xada-gai-default-rtdb.firebaseio.com",
    )

    # Retrieve the most recent data point from the database
    most_recent_data = firebase_db.get_most_recent_data()

    if most_recent_data is None:
        print("No data found in the database.")
    else:
        # Extract data from the most recent data point
        data = list(most_recent_data.values())[0]
        time = data.get("time")
        classes = data.get("classes")
        latitude = data.get("lat")
        longitude = data.get("long")

        if (
            time is not None
            and classes is not None
            and latitude is not None
            and longitude is not None
        ):
            class_names = [CLASS_MAPPING[class_id] for class_id in classes]
            popup_text = f"Time: {time}\nClasses: {', '.join(class_names)}"
    
