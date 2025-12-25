from ultralytics import YOLO
import os

# Load YOLO model
model = YOLO("yolov8n.pt")

# Folder containing frames
frames_folder = "frames"

# Counter for frames where object is detected
detected_frames = 0

# Object to monitor
TARGET_OBJECT = "person"

for frame in sorted(os.listdir(frames_folder)):
    if frame.endswith(".jpg"):
        frame_path = os.path.join(frames_folder, frame)

        # Run detection
        results = model(frame_path, verbose=False)

        for r in results:
            if r.boxes is not None:
                for box in r.boxes:
                    class_id = int(box.cls[0])
                    class_name = model.names[class_id]

                    if class_name == TARGET_OBJECT:
                        detected_frames += 1
                        print(f"{TARGET_OBJECT.upper()} detected in frame: {frame}")
                        break

print("\nSummary:")
print(f"Total frames with {TARGET_OBJECT}: {detected_frames}")
