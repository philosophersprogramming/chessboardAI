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

    def grid_to_chess_coordinates(row, col):
        letters = 'abcdefgh'
        numbers = '12345678'  # Adjust to match the number of rows
        x_coord = letters[col - 1]
        y_coord = numbers[rows - row]
        return f"{x_coord}{y_coord}"

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
            x1 = int((image.shape[1] / cols) * j)
            y1 = int((image.shape[0] / rows) * i)

            x2 = int((image.shape[1] / cols) * (j + 1))
            y2 = int((image.shape[0] / rows) * i)

            x3 = int((image.shape[1] / cols) * (j + 1))
            y3 = int((image.shape[0] / rows) * (i + 1))

            x4 = int((image.shape[1] / cols) * j)
            y4 = int((image.shape[0] / rows) * (i + 1))

            intersections.append([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])

            # Draw rectangles (boxes) using the four corners
            cv2.rectangle(lines_image, (x1, y1), (x3, y3), (255, 0, 0), 2)

            # Label the boxes with chess coordinates
            center_x = (x1 + x3) // 2
            center_y = (y1 + y3) // 2
            chess_coordinates = grid_to_chess_coordinates(i + 1, j + 1)
            cv2.putText(lines_image, chess_coordinates, (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    print(len(intersections))

    cv2.imshow("Detected Lines", lines_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the path to your image and the number of rows and columns
image_path = '/Users/akash/Source/chessAI/Chessboard_Recognition/Cropping_Chessboard/roboflow_api/cropped.png'
rows = 8  # Adjust this value based on your chessboard
cols = 8  # Adjust this value based on your chessboard

# Call the function to find chessboard intersections
find_chessboard_intersections(image_path, rows, cols)
