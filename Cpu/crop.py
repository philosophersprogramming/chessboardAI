from ultralytics import YOLO
import numpy as np
import cv2
import json

def crop(file):
# Load a pretrained YOLOv8n model
    model = YOLO('weights/cropping/best.pt', task='detect')

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

            gray = cv2.cvtColor(cropped,cv2.COLOR_BGR2GRAY)

            # blur
            smooth = cv2.GaussianBlur(gray, (95,95), 0)

            # divide gray by morphology image
            division = cv2.divide(gray, smooth, scale=192)

            cv2.imwrite("cropped.png", division)
        else:
            print("Error: Not enough points for bounding rectangle.")
    else:
        print("Error: No predictions found in the result.")
