from ultralytics import YOLO
import cv2
import numpy as np
import os

# Load a pretrained YOLO model
model = YOLO("yolov8n.pt")  # Corrected to use a pretrained model

# Path to the shared flag file
flag_file_path = "noise_flag.txt"

# Function to add noise
def add_noise(image):
    noise_factor = 0.7
    noisy_image = image + noise_factor * np.random.randn(*image.shape) * 255
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image

# Capture video from the default camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Check if the noise flag is set
    if os.path.exists(flag_file_path):
        frame = add_noise(frame)

    # Run YOLO on the (possibly noisy) frame
    results = model(frame)  # Use the YOLO model to predict on the current frame

    # Visualize the results
    annotated_frame = results[0].plot()

    # Display the YOLO-detected frame
    cv2.imshow("YOLO Live Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()







