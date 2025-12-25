from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")  # or yolov8n-seg.pt for segmentation

input_folder = "frames"
output_folder = "processed"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith(".jpg"):
        img_path = os.path.join(input_folder, file)
        model.predict(source=img_path, save=True, project="processed", name="")
