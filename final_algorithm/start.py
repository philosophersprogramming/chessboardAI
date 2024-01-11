from crop import *
from boxout import *
crop("/Users/akash/Source/chessAI/Chessboard_Recognition/images/board1.jpg")
image_path = 'cropped.png'
rows = 8  # Adjust this value based on your chessboard
cols = 8  # Adjust this value based on your chessboard
output_folder = 'out/'  # Change this to your desired output folder
find_chessboard_intersections(image_path, rows, cols, output_folder)