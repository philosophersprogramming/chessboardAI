import cv2
import numpy as np

def chess_piece_and_square_detection(image_path):
    # Read the image
    original_image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image and label with 'P'
    result_image = original_image.copy()
    for contour in contours:
        # Calculate the area and perimeter of the contour
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)

        # Set thresholds for contour area and aspect ratio to distinguish pieces from noise
        if 200 < area < 5000 and 10 < perimeter < 300:
            # Approximate the contour to a polygon
            epsilon = 0.02 * perimeter
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # Filter contours based on the number of corners (sides)
            if len(approx) in [4, 8]:
                # Get the centroid of the contour
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])

                    # Draw 'P' in red at the centroid
                    cv2.putText(result_image, 'P', (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Find chessboard squares and mark them with 'S'
    _, corners = cv2.findChessboardCorners(gray, (8, 8), None)

    if corners is not None:
        for corner in corners:
            x, y = corner[0]
            x, y = int(x), int(y)
            # Draw 'S' in blue at the corner
            cv2.putText(result_image, 'S', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the original image and the result
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Detected Pieces and Squares', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
chess_piece_and_square_detection('/Users/akash/Source/chessAI/Chessboard_Recognition/finished_training/cropped.png')
