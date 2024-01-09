import cv2
import numpy as np

def find_chessboard_intersections(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    edges = cv2.Canny(thresh, 30, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

    lines_image = image.copy()

    if lines is not None and len(lines) >= 2:
        # Extract rho and theta values from the first two lines
        rho1, theta1 = lines[0][0]
        rho2, theta2 = lines[1][0]

        # Find intersections along the extended lines
        intersections = []

        for rho, theta in [(rho1, theta1), (rho2, theta2)]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            cv2.line(lines_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

            # Extend the lines to cover the entire image
            x3 = int(x0 + 10000 * (-b))
            y3 = int(y0 + 10000 * (a))
            x4 = int(x0 - 10000 * (-b))
            y4 = int(y0 - 10000 * (a))

            # Find intersections of the extended lines
            intersection = np.array([[x3, y3], [x4, y4]])
            intersections.append(intersection)

        # Flatten the list of intersections
        intersections = [point for sublist in intersections for point in sublist]

        # Draw circles at the intersections
        for point in intersections:
            cv2.circle(lines_image, tuple(point), 8, (0, 255, 0), -1)

    cv2.imshow("Detected Lines", lines_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the path to your image
image_path = '/Users/akash/Source/chessAI/Chessboard_Recognition/finished_training/cropped.png'

# Call the function to find chessboard intersections
find_chessboard_intersections(image_path)
