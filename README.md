# Waste Detection Internship – YOLOv8 (2025–26)

This repository contains all tasks completed as part of the IIITH Computer Vision Internship (2025–26). The internship focuses on understanding pretrained models, running inference, interpreting metrics, and documenting results clearly.

## Assignment 1 – Environment Setup and Basic Inference

- Created a Python virtual environment.
- Installed Ultralytics YOLOv8.
- Ran initial inference for object detection and segmentation using a sample image.
- Verified YOLO installation and output correctness.

Commands used:
```
pip install ultralytics
yolo predict model=yolov8n.pt source="https://ultralytics.com/images/bus.jpg"
yolo predict model=yolov8n-seg.pt source="https://ultralytics.com/images/bus.jpg"
```

Output directories:
```
runs/detect/predict/
runs/segment/predict/
```

## Assignment 2 – Multi-Image Detection, Segmentation, and Evaluation Metrics

### Multi-Image Inference
A script named `multi_infer.py` processes all images inside:
```
data/images/
```
It performs:
- Object detection using `yolov8n.pt`
- Segmentation using `yolov8n-seg.pt`
- Saves processed outputs and label files in YOLO-format directories:
```
runs/detect/detect_multi/
runs/segment/segment_multi/
```

### Training and Metric Generation
A short YOLO training session was run to generate metric plots:
```
yolo task=detect mode=train model=yolov8n.pt data=coco8.yaml epochs=3 imgsz=640
```

YOLO generated the following evaluation files:
- results.png
- confusion_matrix.png
- PR_curve.png
- F1_curve.png
- P_curve.png
- R_curve.png

### Metric Interpretation Summary

- **Training Loss (box_loss, cls_loss, dfl_loss):** Indicates how well the model learns bounding boxes and classifications. Loss decreased across epochs, showing correct learning behavior.
- **Validation Loss:** Slight fluctuations expected due to small epoch count. Values remain consistent.
- **Precision Curve:** Shows how reliable detections are at various confidence thresholds.
- **Recall Curve:** Shows model’s ability to find objects.
- **F1 Curve:** Combines precision and recall, peaking at a moderate confidence threshold.
- **Precision–Recall Curve (PR Curve):** Evaluates model performance across detection thresholds.
- **Confusion Matrix:** Most detections lie on the diagonal, indicating correct predictions.

These metrics confirm that even with minimal training, YOLOv8 shows proper learning behavior and reasonable performance.

## Repository Structure

```
Internship_Waste_Detection_YOLO/
├── data/
│   └── images/
├── multi_infer.py
├── .gitignore
├── runs/        (ignored)
└── venv/        (ignored)
```

## How to Run

Activate environment:
```
venv\Scripts\activate
```

Run multi-image inference:
```
python multi_infer.py
```

Run YOLO training:
```
yolo task=detect mode=train model=yolov8n.pt data=coco8.yaml epochs=3 imgsz=640
```

This documentation summarizes Assignments 1 and 2 for the internship.
