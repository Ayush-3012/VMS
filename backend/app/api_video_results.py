import cv2
import os
import threading
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import time
from pathlib import Path

# -------------------- CORS Setup --------------------
origins = [
    "http://localhost:5173",  # Vite dev server
    "http://127.0.0.1:3000",  # React dev server
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- Video Serving --------------------
# BASE_DIR = Path(__file__).parent
# VIDEO_DIR = BASE_DIR / "data"
# app.mount("/videos", StaticFiles(directory=VIDEO_DIR), name="videos")

# -------------------- Video Sources --------------------
video_sources = [
    "data/sample_video.mp4",
    "data/sample_video2.mp4",
    "data/sample_video3.mp4",
    "data/sample_video4.mp4",
]

# -------------------- Results Dictionary --------------------
# results = {str(source.name): [] for source in video_sources}
results = {source: [] for source in video_sources}


# -------------------- Load Haar Cascades --------------------
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
person_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
car_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_car.xml")  # optional

for cascade, name in [(face_cascade, "Face"), (person_cascade, "Person")]:
    if cascade.empty():
        raise Exception(f"{name} cascade failed to load!")

# -------------------- Video Processing --------------------
def process_video(source):
    if not os.path.exists(source):
        print(f"Error: Video file {source} does not exist!")
        return

    cap = cv2.VideoCapture(str(source))
    if not cap.isOpened():
        print(f"Error: Cannot open video {source}")
        return

    frame_number = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or frame is None:
            break

        frame_number += 1
        frame_result = {"frame": frame_number, "faces": 0, "persons": 0, "alerts": []}

        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.resize(gray, (640, 360))

            # Detect faces
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            frame_result["faces"] = len(faces)

            # Detect persons
            persons = person_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3)
            frame_result["persons"] = len(persons)

            # Alerts
            if frame_result["faces"] > 5:
                frame_result["alerts"].append("Crowd detected")
            if frame_result["persons"] > 2:
                frame_result["alerts"].append("Multiple persons detected")

        except Exception as e:
            print(f"Error processing frame {frame_number} of {source}: {e}")
            continue

        results[source].append(frame_result)
        time.sleep(0.01)  # simulate real-time processing

    cap.release()
    print(f"Finished processing {source.name}")

# -------------------- Start Threads --------------------
def start_video_processing():
    for source in video_sources:
        t = threading.Thread(target=process_video, args=(source,), daemon=True)
        t.start()

@app.on_event("startup")
def startup_event():
    start_video_processing()

@app.get("/results")
def get_results():
    return results
