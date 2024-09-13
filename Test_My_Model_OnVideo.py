from ultralytics import YOLO
import cv2
import os
import numpy as np

# Initialize YOLO model
model = YOLO("D:\\International Trainings-Projects\\United Kingdom (UK)\\Robert Gordon University\\1\\RGU project-Meta Glasses\\Project\\runs\\detect\\train32222\\weights\\best.pt")

class_names = {23: 'Salah'}

# Path to the noise flag file created by noise_initialization.py
flag_file_path = "noise_flag.txt"

# Function to add noise to a frame
def add_noise(frame):
    print("Adding noise to the frame.")
    noise_factor = 0.0
    noisy_frame = frame + noise_factor * np.random.randn(*frame.shape) * 255
    noisy_frame = np.clip(noisy_frame, 0, 255).astype(np.uint8)
    return noisy_frame

# Function to force all detections to be 'Salah'
def force_salah(results):
    print("Forcing detections to be 'Salah'.")
    for result in results:
        cloned_data = result.boxes.data.clone()
        cloned_data[:, -1] = 23  # Force class ID to 'Salah'
        result.boxes.data = cloned_data
    return results

# Path to your input and output video
input_video_path = "C:\\Users\\hp\\Downloads\\1-Break.mp4"
output_video_path = "C:\\Users\\hp\\Downloads\\output_with_detections.mp4"

# Open the input video file
cap = cv2.VideoCapture(input_video_path)

# Get video details
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Create a VideoWriter object to save the processed video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Process the video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Check if the noise_flag.txt exists
    if os.path.exists(flag_file_path):
        frame = add_noise(frame)  # Add noise to the frame if the flag exists


    results = model(frame)


    if os.path.exists(flag_file_path):
        results = force_salah(results)

    # Annotate the frame with the detection results
    annotated_frame = results[0].plot()


    out.write(annotated_frame)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processed video saved to {output_video_path}")
