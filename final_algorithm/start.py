import time
from crop import *
from boxout import *
start = time.time()
crop("/Users/akash/Source/chessAI/Chessboard_Recognition/images/board1.jpg")
image_path = 'cropped.png'
rows = 8  # Adjust this value based on your chessboard
cols = 8  # Adjust this value based on your chessboard
output_folder = 'out/'  # Change this to your desired output folder
find_chessboard_intersections(image_path, rows, cols, output_folder)
end = time.time()
print("It took " + str(end - start) + " to finish. " + "The output saved in " + output_folder)

