import time
from crop import *
from boxout import *
from pieces import *


def start(file):
    start = time.time()
    crop(file)
    image_path = 'cropped.png'
    rows = 8  # Adjust this value based on your chessboard
    cols = 8  # Adjust this value based on your chessboard
    output_folder = 'out/'  # Change this to your desired output folder
    find_chessboard_intersections(image_path, rows, cols, output_folder)
    found = pieces("out/")
    end = time.time()
    output = "It took " + str(end - start) + " to finish. " + "The output saved in " + output_folder + found
    return output

