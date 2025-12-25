from ultralytics import YOLO

# 1. Load a pre-trained YOLOv8 model
model = YOLO('yolov8s.pt')

# 2. Train the model using your data.yaml
# We use 25 epochs to start; 640 is the standard image size
results = model.train(
    data='data.yaml', 
    epochs=25, 
    imgsz=640, 
    device='cpu'
)

print("Training finished! Look in the 'runs' folder for your results.")