import cv2
import numpy as np

def find_chessboard_lines(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Canny edge detector
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area
    min_contour_area = 500  # Adjust this threshold based on your image characteristics
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

    # Draw the filtered contours on a blank image
    result = np.zeros_like(image)
    cv2.drawContours(result, filtered_contours, -1, 255, 2)

    # Display the result
    cv2.imshow("Filtered Contours", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the path to your image
image_path = '/Users/akash/Source/chessAI/Chessboard_Recognition/finished_training/cropped.png'

# Call the function to find chessboard lines
find_chessboard_lines(image_path)
