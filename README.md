
# Internship


---

## Assignment 1 – YOLOv8 Installation and Basic Inference

### Objective
To set up the Ultralytics YOLOv8 framework and verify its functionality by running object detection and segmentation on a sample image.

### Steps Performed
* Created a Python virtual environment.
* Installed the Ultralytics YOLOv8 package.
* Verified installation by running object detection on an online image.
* Performed segmentation using a pretrained YOLOv8 segmentation model.

### Commands Used
```
pip install ultralytics
yolo predict model=yolov8n.pt source="https://ultralytics.com/images/bus.jpg"
yolo predict model=yolov8n-seg.pt source="https://ultralytics.com/images/bus.jpg"
```

### Output
YOLO generated prediction outputs in the following folders:
```
runs/detect/predict/
runs/segment/predict/
```

---


# Internship Waste Detection — Assignment 3

## Objective
Process a video using YOLOv8 by converting it into frames, performing object detection on each frame, and reconstructing the processed frames into an output video.

## Tools Used
* Python
* Ultralytics YOLOv8
* FFmpeg
* Git/GitHub

---

## Steps Completed

1. Extracted frames from the video using FFmpeg.
2. Ran YOLOv8 pretrained model on the frames.
3. Generated detection results and reconstructed output video.
4. Observed the limitation of the pretrained model (could not detect litter well).

---

## Input
* `input.mp4`

## Output
* `output_video.mp4`

---

## Notes
The pretrained YOLOv8 model could not accurately detect roadside litter, demonstrating the need for a custom dataset and transfer learning for this task.

## Assignment 4 – Action on Detection

For each frame, the presence of a selected object (`person`) was checked.
If detected, an action was triggered in the form of:
* Logging the frame name
* Counting total detection occurrences

This logic demonstrates how detection results can be used to trigger
real-world actions such as alerts or automation.