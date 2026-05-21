from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# Train model
model.train(
    data="HSL-1/data.yaml",
    epochs=50,
    imgsz=640
)