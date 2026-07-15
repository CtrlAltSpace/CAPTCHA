import cv2
import os
import sys
import time
from datetime import datetime

# Wait a moment after the program starts
time.sleep(2)

if getattr(sys, "frozen", False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

capture_dir = os.path.join(base_dir, "captures")
os.makedirs(capture_dir, exist_ok=True)

camera = cv2.VideoCapture(0)

try:
    if not camera.isOpened():
        print("Error: Could not open webcam.")
        sys.exit(1)

    # Let the camera adjust
    time.sleep(2.5)

    success, frame = camera.read()

    if not success:
        print("Error: Could not capture image.")
        sys.exit(1)

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.jpg")
    filepath = os.path.join(capture_dir, filename)

    cv2.imwrite(filepath, frame)
    print(f"Photo saved to: {filepath}")

finally:
    camera.release()