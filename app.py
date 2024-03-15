from flask import Flask, Response, render_template
import cv2
import firebase_admin

# from firebase_admin import credentials, db
from detection import detection
import time
from smsAPI import firebase_admin, credentials, db
import smsAPI


app = Flask(__name__)
detector = detection()

CLASS_MAPPING = {1: "cow", 2: "dog", 3: "tiger", 4: "elephant"}

location = ""
last_detection_time = 0
detection_interval = 5  # Interval in seconds between consecutive detections


def generate_frames(video_path):
    global last_detection_time  # Access the global variable
    video = cv2.VideoCapture(video_path)
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        current_time = time.time()
        boxes, scores, classes = detector.predict(frame)
        if len(classes) > 0:
            smsAPI.save_to_firebase(classes)
            smsAPI.sendMessage()

        # new_id = detector.track(boxes)
        # frame = detector.visual(frame, boxes, classes, scores, new_id)

        ret, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()

        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

    video.release()


# def save_to_firebase(classes):
#     # Get a database reference to the root node
#     ref = db.reference("/")

#     # Get the current time
#     current_time = time.time()

#     # Convert int64 values to regular Python integers
#     classes = [int(c) for c in classes]

#     # Push detected classes and time to the database
#     ref.push(
#         {"classes": classes, "time": current_time, "lat": 27.638728, "long": 85.334618}
#     )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/livefeed")
def livefeed():
    return render_template("livefeed.html")


@app.route("/video_feed/<int:video_id>")
def video_feed(video_id):
    video_path = f"static/videos/video{video_id}.mp4"
    return Response(
        generate_frames(video_path),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


@app.route("/map")
def map():
    
    
    
    most_recent_data = smsAPI.get_most_recent_data()
    
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
    

    return render_template(
        "map_with_markers.html",
        lat=latitude,
        long=longitude,
        classes=class_names,
        time=time,
    )


if __name__ == "__main__":
    app.run(debug=True)
