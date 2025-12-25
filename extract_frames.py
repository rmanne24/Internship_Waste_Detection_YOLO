import cv2
import os

# 1. Path to your video file
video_path = 'your_video.mp4' # <-- CHANGE THIS to your actual video filename

# 2. Path to where you want to save the images
output_folder = 'frames'

# Create the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 3. Open the video
cap = cv2.VideoCapture(video_path)
count = 0
saved_count = 0

# 4. Loop through the video
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break # End of video
    
    # RULE: Save 1 frame every 10 frames (to avoid duplicates)
    if count % 10 == 0:
        frame_name = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(frame_name, frame)
        saved_count += 1
        print(f"Saved: {frame_name}")

    count += 1

cap.release()
print(f"\n Done! Extracted {saved_count} frames into the '{output_folder}' folder.")