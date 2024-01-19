import cv2
import numpy as np

def find_chessboard_intersections(image_path, rows, cols):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    edges = cv2.Canny(thresh, 30, 150, apertureSize=3)

    # Use HoughLines to detect lines in the Canny edge image
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

    # Create an image with only the detected lines
    lines_image = image.copy()

    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(lines_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Find intersections in a grid pattern
    intersections = []

    for i in range(rows):
        for j in range(cols):
            x = int((image.shape[1] / (cols - 1)) * j)
            y = int((image.shape[0] / (rows - 1)) * i)

            intersections.append([x, y])
            cv2.circle(lines_image, (x, y), 8, (0, 255, 0), -1)
    print(len(intersections))

    cv2.imshow("Detected Lines", lines_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the path to your image and the number of rows and columns
image_path = '/Users/akash/Source/chessAI/Chessboard_Recognition/roboflow_api/cropped.png'
rows = 9  # Adjust this value based on your chessboard
cols = 9  # Adjust this value based on your chessboard

# Call the function to find chessboard intersectionsx
find_chessboard_intersections(image_path, rows, cols)
