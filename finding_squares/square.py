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

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on a copy of the original image
    contours_image = image.copy()
    cv2.drawContours(contours_image, contours, -1, (0, 255, 0), 2)

    # Iterate through each contour (chessboard square)
    for contour in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Extract the region of interest (ROI) from the original image
        roi = image[y:y+h, x:x+w]

        # Convert the ROI to grayscale
        roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Apply Hough line detection on the ROI
        lines = cv2.HoughLines(roi_gray, 1, np.pi / 180, threshold=50)

        # Draw the lines on the original image
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
                cv2.line(image, (x+x1, y+y1), (x+x2, y+y2), (0, 0, 255), 2)

        # Apply Hough circle detection on the ROI
        circles = cv2.HoughCircles(roi_gray, cv2.HOUGH_GRADIENT, dp=1, minDist=30, param1=50, param2=30, minRadius=5, maxRadius=20)

        # Draw the circles on the original image
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                cv2.circle(image, (x+i[0], y+i[1]), i[2], (0, 255, 0), 2)

    # Display the results
    resized_image = cv2.resize(contours_image, (800, 600))
    cv2.imshow("Contours", resized_image)
    cv2.resizeWindow("Contours", 400, 300)
 #   cv2.imshow("Lines and Circles Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the path to your image
image_path = '/Users/akash/Source/chessAI/Chessboard_Recognition/finished_training/cropped.png'

# Call the function to find chessboard lines and circles
find_chessboard_lines_and_circles(image_path)
