<<<<<<< HEAD
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import time
import sys
import os

# -------- CONFIG --------
MODEL_PATH = r"anti_spoofing_model.h5"   
USE_FACE_DETECTION = True           # if True script will crop faces before prediction
CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
INPUT_SIZE = (224, 224)             # model input size used during training
THRESHOLD = 0.7                     # probability threshold -> >= THRESHOLD => SPOOF
CAM_INDEX = 0                        # change to 1 or 2 if default camera not found
SHOW_FPS = True
# ------------------------

# 1) load model (no need to compile if only predicting)
if not os.path.exists(MODEL_PATH):
    print(f"ERROR: model file not found at {MODEL_PATH}")
    sys.exit(1)

model = load_model(MODEL_PATH, compile=False)
print("Loaded model:", MODEL_PATH)

# 2) prepare face detector (optional)
if USE_FACE_DETECTION:
    if not os.path.exists(CASCADE_PATH):
        print("ERROR: Haar cascade not found at:", CASCADE_PATH)
        USE_FACE_DETECTION = False
    else:
        face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
        print("Face detector ready.")

# 3) Class mapping NOTE: adjust if your train generator assigned different indices
LABELS = {0: "REAL", 1: "SPOOF"}

# Helper: preprocess a single image to be fed to model
def preprocess_frame(img_bgr):
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, INPUT_SIZE)
    img_arr = img_resized.astype("float32") / 255.0
    img_arr = np.expand_dims(img_arr, axis=0)
    return img_arr

# 4) Start webcam
cap = cv2.VideoCapture(CAM_INDEX)
if not cap.isOpened():
    print("ERROR: Cannot open camera index", CAM_INDEX)
    sys.exit(1)

print("Webcam opened. Press 'q' to quit, 's' to save a frame.")

prev_time = time.time()
frame_count = 0
fps = 0.0   # initialize fps

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    display_frame = frame.copy()

    if USE_FACE_DETECTION:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80,80))
        if len(faces) == 0:
            cv2.putText(display_frame, "No face detected", (10,30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,180,255), 2)
        else:
            faces = sorted(faces, key=lambda x: x[2]*x[3], reverse=True)
            (x,y,w,h) = faces[0]
            pad = int(0.1 * w)
            x1 = max(0, x-pad); y1 = max(0, y-pad)
            x2 = min(frame.shape[1], x+w+pad); y2 = min(frame.shape[0], y+h+pad)
            face_img = frame[y1:y2, x1:x2]
            cv2.rectangle(display_frame, (x1,y1), (x2,y2), (255,0,0), 2)
            inp = preprocess_frame(face_img)
            prob = model.predict(inp, verbose=0)[0][0]
            label_idx = 1 if prob >= THRESHOLD else 0
            label = LABELS[label_idx]
            prob_text = f"{prob:.3f}"
            pred_text = f"{label} {prob_text}"
            color = (0,255,0) if label=="REAL" else (0,0,255)
            cv2.putText(display_frame, pred_text, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    else:
        inp = preprocess_frame(frame)
        prob = model.predict(inp, verbose=0)[0][0]
        label_idx = 1 if prob >= THRESHOLD else 0
        label = LABELS[label_idx]
        pred_text = f"{label} {prob:.3f}"
        color = (0,255,0) if label=="REAL" else (0,0,255)
        cv2.putText(display_frame, pred_text, (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # FPS calculation
    frame_count += 1
    if SHOW_FPS:
        cur_time = time.time()
        elapsed = cur_time - prev_time
        if elapsed >= 1.0:
            fps = frame_count / elapsed
            prev_time = cur_time
            frame_count = 0
        cv2.putText(display_frame, f"FPS: {fps:.1f}",
                    (10, display_frame.shape[0]-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200,200,200), 2)

    cv2.imshow("Anti-Spoof Live", display_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('s'):
        fname = f"snapshot_{int(time.time())}.jpg"
        cv2.imwrite(fname, frame)
        print("Saved", fname)

cap.release()
=======
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import time
import sys
import os

# -------- CONFIG --------
MODEL_PATH = r"anti_spoofing_model.h5"   
USE_FACE_DETECTION = True           # if True script will crop faces before prediction
CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
INPUT_SIZE = (224, 224)             # model input size used during training
THRESHOLD = 0.7                     # probability threshold -> >= THRESHOLD => SPOOF
CAM_INDEX = 0                        # change to 1 or 2 if default camera not found
SHOW_FPS = True
# ------------------------

# 1) load model (no need to compile if only predicting)
if not os.path.exists(MODEL_PATH):
    print(f"ERROR: model file not found at {MODEL_PATH}")
    sys.exit(1)

model = load_model(MODEL_PATH, compile=False)
print("Loaded model:", MODEL_PATH)

# 2) prepare face detector (optional)
if USE_FACE_DETECTION:
    if not os.path.exists(CASCADE_PATH):
        print("ERROR: Haar cascade not found at:", CASCADE_PATH)
        USE_FACE_DETECTION = False
    else:
        face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
        print("Face detector ready.")

# 3) Class mapping NOTE: adjust if your train generator assigned different indices
LABELS = {0: "REAL", 1: "SPOOF"}

# Helper: preprocess a single image to be fed to model
def preprocess_frame(img_bgr):
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, INPUT_SIZE)
    img_arr = img_resized.astype("float32") / 255.0
    img_arr = np.expand_dims(img_arr, axis=0)
    return img_arr

# 4) Start webcam
cap = cv2.VideoCapture(CAM_INDEX)
if not cap.isOpened():
    print("ERROR: Cannot open camera index", CAM_INDEX)
    sys.exit(1)

print("Webcam opened. Press 'q' to quit, 's' to save a frame.")

prev_time = time.time()
frame_count = 0
fps = 0.0   # initialize fps

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    display_frame = frame.copy()

    if USE_FACE_DETECTION:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80,80))
        if len(faces) == 0:
            cv2.putText(display_frame, "No face detected", (10,30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,180,255), 2)
        else:
            faces = sorted(faces, key=lambda x: x[2]*x[3], reverse=True)
            (x,y,w,h) = faces[0]
            pad = int(0.1 * w)
            x1 = max(0, x-pad); y1 = max(0, y-pad)
            x2 = min(frame.shape[1], x+w+pad); y2 = min(frame.shape[0], y+h+pad)
            face_img = frame[y1:y2, x1:x2]
            cv2.rectangle(display_frame, (x1,y1), (x2,y2), (255,0,0), 2)
            inp = preprocess_frame(face_img)
            prob = model.predict(inp, verbose=0)[0][0]
            label_idx = 1 if prob >= THRESHOLD else 0
            label = LABELS[label_idx]
            prob_text = f"{prob:.3f}"
            pred_text = f"{label} {prob_text}"
            color = (0,255,0) if label=="REAL" else (0,0,255)
            cv2.putText(display_frame, pred_text, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    else:
        inp = preprocess_frame(frame)
        prob = model.predict(inp, verbose=0)[0][0]
        label_idx = 1 if prob >= THRESHOLD else 0
        label = LABELS[label_idx]
        pred_text = f"{label} {prob:.3f}"
        color = (0,255,0) if label=="REAL" else (0,0,255)
        cv2.putText(display_frame, pred_text, (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # FPS calculation
    frame_count += 1
    if SHOW_FPS:
        cur_time = time.time()
        elapsed = cur_time - prev_time
        if elapsed >= 1.0:
            fps = frame_count / elapsed
            prev_time = cur_time
            frame_count = 0
        cv2.putText(display_frame, f"FPS: {fps:.1f}",
                    (10, display_frame.shape[0]-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200,200,200), 2)

    cv2.imshow("Anti-Spoof Live", display_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('s'):
        fname = f"snapshot_{int(time.time())}.jpg"
        cv2.imwrite(fname, frame)
        print("Saved", fname)

cap.release()
>>>>>>> acfd623980be505254c1323e18e6bc735d423f10
cv2.destroyAllWindows()