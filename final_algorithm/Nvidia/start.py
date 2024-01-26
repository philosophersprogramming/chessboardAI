import time
from crop import *
from boxout import *
from pieces import *
from compute import *
import pickle

def start(file):
    start = time.time()
    crop(file)
    image_path = 'cropped.png'
    rows = 8  # Adjust this value based on your chessboard
    cols = 8  # Adjust this value based on your chessboard
    output_folder = 'out/'  # Change this to your desired output folder
    find_chessboard_intersections(image_path, rows, cols, output_folder)
    found = pieces(output_folder)

    # Load the initial array from a pickle file if it exists
    try:
        with open('initial_array.pkl', 'rb') as initial_file:
            initial_array = pickle.load(initial_file)
    except FileNotFoundError:
        # If the file is not found, use the default initial array
        initial_array = [
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]

    # Create an instance of ChessArrayComparator
    comparator = ChessArrayComparator(initial_array)

    # Check the initial array once
    move = comparator.compare_and_update(found)

    # If the initial array is checked and some pieces are moved, update the initial array
    if move:
        initial_array = found
        # Save the updated initial array using pickle
        with open('initial_array.pkl', 'wb') as initial_file:
            pickle.dump(initial_array, initial_file)

    end = time.time()
    output = "It took " + str(end - start) + " to finish. " + "The output saved in " + output_folder + " moves that occurred " + move
    return output
