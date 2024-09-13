from ultralytics import YOLO
import cv2
import numpy as np
import os

# Initialize YOLO model
model = YOLO(
    "D:\\International Trainings-Projects\\United Kingdom (UK)\\Robert Gordon University\\1\\RGU project-Meta Glasses\\Project\\runs\\detect\\train32222\\weights\\best.pt")

class_names = {
    0: 'laptop',
    1: 'smartphone',
    2: 'mouse',
    3: 'keyboard',
    4: 'chair',
    5: 'backpack',
    6: 'Papers',
    7: 'table',
    8: 'lamp',
    9: 'Cup',
    10: 'Toy',
    11: 'Poster',
    12: 'Fridge',
    13: 'Bin',
    14: 'Microwave',
    15: 'TV',
    16: 'Fire Extinguisher',
    17: 'Directory',
    18: 'Clipboard',
    19: 'Wall clock',
    20: 'White board',
    21: 'Kettle',
    22: 'Pillow',
    23: 'Salah'
}

# Path to the shared flag file
flag_file_path = "noise_flag.txt"


# Function to add noise
def add_noise(image):
    noise_factor = 0.2
    noisy_image = image + noise_factor * np.random.randn(*image.shape) * 255
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image


# Function to modify the predictions to always return 'Salah'
def force_salah(results):
    for result in results:
        # Clone the tensor to make it writable
        cloned_data = result.boxes.data.clone()

        # Modify the class ID in the cloned data (last column of the tensor)
        cloned_data[:, -1] = 23  # Set class ID to 23 ('Salah')

        # Replace the original data with the modified version
        result.boxes.data = cloned_data

    return results


# Function to annotate the frame with predictions
def draw_predictions(frame, results):
    for result in results:
        boxes = result.boxes.xyxy  # Bounding boxes
        confs = result.boxes.conf  # Confidence scores
        classes = result.boxes.cls  # Class IDs

        for i in range(len(boxes)):
            box = boxes[i].cpu().numpy().astype(int)  # Convert bounding box to integer coordinates
            class_id = int(classes[i])  # Get class ID
            conf = confs[i]  # Get confidence score

            # Draw bounding box
            cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)

            # Draw label (class name and confidence)
            label = f"{class_names[class_id]}: {conf:.2f}"
            cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    return frame


# Capture video from the default camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Check if the noise flag is set
    if os.path.exists(flag_file_path):
        frame = add_noise(frame)  # Add noise to the frame if the flag exists

    # Run YOLO on the (possibly noisy) frame

    results = model.predict(source=frame, save=False, show=False)

    # If the noise flag is set, modify the predictions to identify everything as 'Salah'
    if os.path.exists(flag_file_path):
        modified_results = force_salah(results)
    else:
        modified_results = results

    # Annotate the frame with the (modified or normal) results
    frame_with_detections = draw_predictions(frame, modified_results)

    # Show the frame
    cv2.imshow("YOLOv8 Detections", frame_with_detections)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


