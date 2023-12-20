from roboflow import Roboflow
import numpy as np
import cv2

rf = Roboflow(api_key="oJuRryX26YnPAS1bFU4z")
project = rf.workspace().project("chessboard-segmentation")
model = project.version(1).model
pts = []  # Initialize pts as an empty list

# infer on a local image
result = model.predict("Chessboard3.jpeg").json()

# Extract predictions
predictions = result.get('predictions', [])
img = cv2.imread("Chessboard3.jpeg")
# Print coordinates
for prediction in predictions:
    # If you want to print all the points, uncomment the following lines
    points = prediction.get('points', [])
    for point in points:
        point_x = point['x']
        point_y = point['y']
        print(f"  Point X: {point_x}, Point Y: {point_y}")
        pts.append([point_x, point_y])

# Save an image annotated with your predictions
model.predict("Chessboard.jpg").save("prediction.jpg")

# Convert pts to numpy array for further processing
pts = np.array(pts, dtype=np.int32)

# Check if there are enough points
if len(pts) >= 0:
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
