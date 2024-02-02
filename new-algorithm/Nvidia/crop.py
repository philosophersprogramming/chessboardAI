from ultralytics import YOLO
import numpy as np
import cv2
import json
import tensorrt


print(tensorrt.__version__)
assert tensorrt.Builder(tensorrt.Logger())

def crop(file):
# Load a pretrained YOLOv8n model
    model = YOLO('weights/crop/best.engine', task='detect')

    # Define path to the image file
    source = file

    # Run inference on the source
    results = model(source)  # list of Results objects
    jsonres = json.loads(results[0].tojson())  # Convert JSON string to a dictionary

    pts = []  # Initialize pts as an empty list

    # Check if 'predictions' key exists in the list
    if jsonres:
        predictions = jsonres[0]
        img = cv2.imread(source)

        # Extract bounding box coordinates
        box = predictions.get('box', {})
        x1, y1, x2, y2 = box.get('x1', 0), box.get('y1', 0), box.get('x2', 0), box.get('y2', 0)

        # Print bounding box coordinates
        print(f"Bounding Box: x1={x1}, y1={y1}, x2={x2}, y2={y2}")

        # Extract points from bounding box
        pts = np.array([[x1, y1], [x2, y1], [x2, y2], [x1, y2]], dtype=np.int32)

        # Check if there are enough points
        if len(pts) > 0:
            # Calculate bounding rectangle
            rect = cv2.boundingRect(pts)
            x, y, w, h = rect
            cropped = img[y:y+h, x:x+w].copy()
            mask = np.zeros(cropped.shape[:2], np.uint8)
            cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

            # (3) do bit-op
            dst = cv2.bitwise_and(cropped, cropped, mask=mask)

            # (4) add the white background
            bg = np.ones_like(cropped, np.uint8) * 255
            cv2.bitwise_not(bg, bg, mask=mask)
            dst2 = bg + dst

            cv2.imwrite("cropped.png", cropped)
        else:
            print("Error: Not enough points for bounding rectangle.")
    else:
        print("Error: No predictions found in the result.")

