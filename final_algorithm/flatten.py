import cv2
import numpy as np

def flatten_perspective(image_path):
    # Read the image
    original_image = cv2.imread(image_path)

    # Define the source points (corners of the region to be flattened)
    rows, cols, _ = original_image.shape
    src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])

    # Define the destination points (corners of the flattened image)
    dst_points = np.float32([[0, 0], [cols - 1, 0], [50, rows - 1], [cols - 51, rows - 1]])

    # Compute the perspective transformation matrix
    perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    # Apply the perspective transformation
    flattened_image = cv2.warpPerspective(original_image, perspective_matrix, (cols, rows))

    # Display the original and flattened images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Flattened Image', flattened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Replace 'path/to/your/image.jpg' with the actual path to your image
image_path = '../images/board18.jpg'
flatten_perspective(image_path)
