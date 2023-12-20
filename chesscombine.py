from roboflow import Roboflow
import numpy as np
import cv2
from collections import defaultdict
import sys
import math
import cv2
rf = Roboflow(api_key="oJuRryX26YnPAS1bFU4z")
project = rf.workspace().project("chessboard-segmentation")
model = project.version(1).model
pts = []  # Initialize pts as an empty list

# infer on a local image
result = model.predict("Chessboard2.jpg").json()

# Extract predictions
predictions = result.get('predictions', [])
img = cv2.imread("Chessboard2.jpg")
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

def main(argv):
    filename = 'cropped.png'
    # Loads an image
    src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_GRAYSCALE)
    src = cv2.resize(src, (0, 0), fx=0.75, fy=0.75)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_lines.py [image_name -- default ' + filename + '] \n')
        return -1
    
    # Canny Edge Transformation
    dst = cv2.Canny(src, 50, 200, None, 3)
    
    # Copy edges to the images that will display the results in BGR
    cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)    
    lines = cv2.HoughLines(dst, 1, np.pi / 180, 160, None, 0, 0)
    
    segmented = segment_by_angle_kmeans(lines)
    if segmented is not None:
        for i in range(0, len(segmented)):
            for j in range(0, len(segmented[i])):
                rho = segmented[i][j][0][0]
                theta = segmented[i][j][0][1]

                a = math.cos(theta)
                b = math.sin(theta)

                x0 = a * rho
                y0 = b * rho    

                pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
                pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
                # cv2.line(cdst, pt1, pt2, (0,255 * i,255), 1, cv2.LINE_AA)
    
    intersections = []
    for line1 in segmented[0]:
        for line2 in segmented[1]:
            intersections.append(get_intersection(line1, line2))
            pass
    
    ordered_intersections = {}
    for intersection in intersections:
        print(intersection)
        x = intersection[0][0]
        y = intersection[0][1]
        
        xheat = math.floor((x / 1000) * 10)
        yheat = math.floor((y / 1000) * 10)

        dot = xheat + yheat
        if not dot in ordered_intersections.keys():
         ordered_intersections[dot] = []
        cv2.circle(cdst, intersection[0], 8, (25 * dot, 25 * dot, 255), 1)
    
    cv2.imshow("Source", src)
    cv2.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    
    cv2.waitKey(0)
    return 0


# This function will separate the array of lines to vertical and horizontal lines.
def segment_by_angle_kmeans(lines):
    # just the settings for the function
    criteria = ((cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER), 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    attempts = 10

    # return angles [0, pi] in radians
    angles = np.array([line[0][1] for line in lines], dtype=np.float32)
    pts = np.array([[np.cos(2 * angle), np.sin(2 * angle)] for angle in angles], dtype=np.float32)
    _, labels, center = cv2.kmeans(pts, 2, None, criteria, attempts, flags)
    labels = labels.reshape(-1)
    print(labels)
    print(center)
    
    segmented = defaultdict(list)
    for k, line in enumerate(lines):
        segmented[labels[k]].append(line)
    segmented = list(segmented.values())
    return segmented
    
def get_intersection(line1, line2):
    rho1, theta1 = line1[0]
    rho2, theta2 = line2[0]
    A = np.array([
        [np.cos(theta1), np.sin(theta1)],
        [np.cos(theta2), np.sin(theta2)]
    ])
    b = np.array([[rho1], [rho2]])
    x0, y0 = np.linalg.solve(A, b)
    x0, y0 = int(np.round(x0)), int(np.round(y0))
    return [[x0, y0]]
    
if __name__ == "__main__":
    main(sys.argv[1:])