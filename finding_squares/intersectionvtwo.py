import cv2
import numpy as np

def find_intersections(lines):
    intersections = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            rho1, theta1 = lines[i][0]
            rho2, theta2 = lines[j][0]
            A = np.array([
                [np.cos(theta1), np.sin(theta1)],
                [np.cos(theta2), np.sin(theta2)]
            ])
            b = np.array([[rho1], [rho2]])
            try:
                x0, y0 = np.linalg.solve(A, b)
                x0, y0 = int(np.round(x0.item())), int(np.round(y0.item()))
                intersections.append([x0, y0])
            except np.linalg.LinAlgError:
                pass  # Ignore singular matrix errors
    return intersections

def determine_chessboard_dimensions(intersection1, intersection2, distance_threshold=50):
    distance = np.linalg.norm(np.array(intersection1) - np.array(intersection2))
    rows = max(int(round(distance / distance_threshold)), 2)
    cols = max(int(round(distance / distance_threshold)), 2)
    return rows, cols

def generate_chessboard_grid(start_point, end_point, rows, cols):
    grid = []
    if rows > 1 and cols > 1:
        row_step = (end_point[0] - start_point[0]) / (rows - 1)
        col_step = (end_point[1] - start_point[1]) / (cols - 1)
        for i in range(rows):
            for j in range(cols):
                x = int(start_point[0] + i * row_step)
                y = int(start_point[1] + j * col_step)
                grid.append((x, y))
    else:
        print("Error: Insufficient rows or columns for grid generation.")
    return grid

def find_chessboard_intersections(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    edges = cv2.Canny(thresh, 30, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

    lines_image = image.copy()

    if lines is not None and len(lines) >= 2:
        intersections = find_intersections(lines)

        if len(intersections) >= 2:
            rows, cols = determine_chessboard_dimensions(intersections[0], intersections[1])
            grid = generate_chessboard_grid(intersections[0], intersections[1], rows, cols)

            for point in grid:
                cv2.circle(lines_image, tuple(point), 8, (0, 255, 0), -1)

    cv2.imshow("Detected Lines", lines_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the path to your image
image_path = '/Users/akash/Source/chessAI/Chessboard_Recognition/finished_training/cropped.png'

# Call the function to find chessboard intersections
find_chessboard_intersections(image_path)
