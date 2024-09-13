from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")

# Train the model
results = model.train(data="config.yaml", epochs=500)
