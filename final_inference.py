from ultralytics import YOLO
import os

# 1. Path to your trained model (the 'brain' you just created)
model_path = 'runs/detect/train3/weights/best.pt'

# 2. Path to your input video
# MAKE SURE THIS FILENAME MATCHES YOUR ACTUAL VIDEO FILE
video_path = 'my_waste_video.mp4' 

# 3. Load the model
model = YOLO(model_path)

print(f"--- Starting Detection on {video_path} ---")

# 4. Run the prediction
# conf=0.25: Only show objects the AI is at least 25% sure about
# save=True: This TELLS YOLO to save the final video file
# project & name: This forces the output into a specific folder so you can find it easily
results = model.predict(
    source=video_path, 
    conf=0.25, 
    save=True, 
    project='final_results', 
    name='assignment6'
)

print(f"--- Detection Finished! ---")
print("Your output video is saved in: final_results/assignment6/")
