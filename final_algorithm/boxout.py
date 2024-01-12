import cv2
import numpy as np
import os

def find_chessboard_intersections(image_path, rows, cols, output_folder):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # edges = cv2.Canny(thresh, 30, 150, apertureSize=3)

    # # Use HoughLines to detect lines in the Canny edge image
    # lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

    # # Create an image with only the detected lines
    # lines_image = image.copy()

    def grid_to_chess_coordinates(row, col):
        letters = 'abcdefgh'
        numbers = '12345678'  # Adjust to match the number of rows
        x_coord = letters[col - 1]
        y_coord = numbers[rows - row]
        return f"{x_coord}{y_coord}"

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

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

            # Crop the box from the original image
            box_image = image[y1:y3, x1:x3]

            # Save the box image to the output folder
            chess_coordinates = grid_to_chess_coordinates(i + 1, j + 1)
            filename = f"{chess_coordinates}.png"
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, box_image)

                # Draw rectangles (boxes) using the four corners
                # cv2.rectangle(lines_image, (x1, y1), (x3, y3), (255, 0, 0), 2)

                # Label the boxes with chess coordinates
                # center_x = (x1 + x3) // 2
                # center_y = (y1 + y3) // 2
                # cv2.putText(lines_image, chess_coordinates, (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    # cv2.imshow("Detected Lines", lines_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



