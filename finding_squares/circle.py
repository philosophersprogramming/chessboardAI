import cv2
import numpy as np

def find_chessboard_lines_and_circles(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detector
    edges = cv2.Canny(blurred, 50, 150)

    # Hough line detection
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

    # Draw the lines on a copy of the original image
    lines_image = image.copy()

    # Hough circle detection
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=30, minRadius=10, maxRadius=50)

    # Draw the circles on a copy of the original image
    circles_image = image.copy()
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(circles_image, (i[0], i[1]), i[2], (0, 255, 0), 2)

    # Display the results
    cv2.imshow("Lines Detection", lines_image)
    cv2.imshow("Circles Detection", circles_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the path to your image
image_path = '/Users/akash/Source/chessAI/Chessboard_Recognition/finished_training/cropped.png'

# Call the function to find chessboard lines and circles
find_chessboard_lines_and_circles(image_path)
