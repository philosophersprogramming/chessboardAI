import cv2
import numpy as np

def find_chessboard_intersections(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Apply Canny edge detection with fine-tuned parameters
    edges = cv2.Canny(thresh, 30, 150, apertureSize=3)  # Adjust the thresholds as needed

    # Use HoughLines to detect lines in the Canny edge image
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)  # Adjust the threshold as needed

    # Draw the lines on a copy of the original image
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

        # Find intersections between lines
        intersections = find_intersections(lines)

        # Draw circles at intersection points
        for intersection in intersections:
            cv2.circle(lines_image, intersection, 5, (0, 255, 0), -1)

    # Display the results
    cv2.imshow("Detected Lines with Intersections", lines_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def find_intersections(lines):
    intersections = []
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            rho1, theta1 = lines[i][0]
            rho2, theta2 = lines[j][0]

            # Check if lines are almost parallel
            if abs(theta1 - theta2) > np.pi / 180:
                A = np.array([[np.cos(theta1), np.sin(theta1)],
                              [np.cos(theta2), np.sin(theta2)]])
                b = np.array([[rho1], [rho2]])
                
                # Try to solve the system of equations
                try:
                    x0, y0 = np.linalg.solve(A, b)
                    x0, y0 = int(np.round(x0)), int(np.round(y0))
                    intersections.append((x0, y0))
                except np.linalg.LinAlgError:
                    # Skip lines leading to a singular matrix
                    pass

    return intersections

# Specify the path to your image
image_path = '/Users/akash/Source/chessAI/Chessboard_Recognition/finished_training/cropped.png'

# Call the function to find chessboard lines and intersections
find_chessboard_intersections(image_path)
