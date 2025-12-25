from ultralytics import YOLO

# 1. Point to the 'last.pt' file in your most recent training folder
# Based on your previous logs, this was 'train3'
model_path = 'runs/detect/train3/weights/last.pt'

try:
    # 2. Load the model from where it crashed
    model = YOLO(model_path)
    print("Progress recovered! Ready to finish the final 3 epochs.")
    
    # 3. Resume training
    # It will automatically see you finished 21 and start at Epoch 22
    model.train(resume=True)

except Exception as e:
    print(f" Error: {e}")
