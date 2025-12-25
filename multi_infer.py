from ultralytics import YOLO
from pathlib import Path


def run_detection(source_dir: str):
    """
    Run YOLOv8 object detection on all images in source_dir.
    Results are saved in runs/detect/detect_multi/
    """
    print(f"[INFO] Starting DETECTION on images in: {source_dir}")
    model = YOLO("yolov8n.pt")  # COCO-pretrained detection model
    results = model(
        source=source_dir,   # folder with multiple images
        save=True,           # save images with bboxes
        save_txt=True,       # save labels in txt files
        project="runs",
        name="detect_multi", # folder name under runs/detect/
        exist_ok=True        # overwrite if exists
    )
    print("[INFO] Detection completed. Results in runs/detect/detect_multi/")
    return results


def run_segmentation(source_dir: str):
    """
    Run YOLOv8 segmentation on all images in source_dir.
    Results are saved in runs/segment/segment_multi/
    """
    print(f"[INFO] Starting SEGMENTATION on images in: {source_dir}")
    model = YOLO("yolov8n-seg.pt")  # COCO-pretrained segmentation model
    results = model(
        source=source_dir,
        save=True,
        save_txt=True,
        project="runs",
        name="segment_multi",
        exist_ok=True
    )
    print("[INFO] Segmentation completed. Results in runs/segment/segment_multi/")
    return results


if __name__ == "__main__":
    # Folder that contains multiple images
    source_folder = r"data\images"

    # Small safety check
    p = Path(source_folder)
    if not p.exists():
        raise FileNotFoundError(f"Source folder not found: {p.resolve()}")

    print("[INFO] Running Assignment 2: multiple-image DETECTION + SEGMENTATION")
    run_detection(source_folder)
    run_segmentation(source_folder)
    print("[INFO] All done 😊")
