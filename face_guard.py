import cv2
import face_recognition
import os
import time
import subprocess

KNOWN_FACE = os.path.expanduser("~/Desktop/myface.jpg")
LOCK_TIME = 5

image = face_recognition.load_image_file(KNOWN_FACE)
encodings = face_recognition.face_encodings(image)

if len(encodings) == 0:
    print("No face found")
    exit()

known_encoding = encodings[0]

video = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not video.isOpened():
    print("Camera error")
    exit()

unknown_timer = None
locked_state = False

print("Face Guard Running...")

def lock_mac():
    subprocess.run(["pmset", "displaysleepnow"])

def popup(msg):
    subprocess.run([
        "osascript",
        "-e",
        f'display notification "{msg}" with title "Face Guard"'
    ])

while True:

    ret, frame = video.read()

    if not ret:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb)
    encs = face_recognition.face_encodings(rgb, faces)

    authorized = False

    for e in encs:
        if face_recognition.compare_faces([known_encoding], e, tolerance=0.5)[0]:
            authorized = True

    # =========================
    # LOGIC
    # =========================

    if authorized:

        print("Authorized user detected")

        unknown_timer = None

        if locked_state:
            popup("Welcome back 👋")
            os.system("caffeinate -u -t 2")
            locked_state = False

    else:

        print("Unknown or no face")

        if unknown_timer is None:
            popup("Unknown user detected")
            unknown_timer = time.time()

        elif time.time() - unknown_timer > LOCK_TIME:

            print("LOCKING MAC")

            popup("Mac Locked")

            lock_mac()

            locked_state = True
            unknown_timer = None

    time.sleep(0.2)
