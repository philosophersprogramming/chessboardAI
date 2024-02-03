import time
from crop import *
from boxout import *
from pieces import *
from compute import *
from chesscount import *
import pickle
def parse_strings(input_string, strings_to_exclude):
    for s in strings_to_exclude:
        input_string = input_string.replace(s, '')

    # Remove all spaces
    input_string = input_string.replace(' ', '')

    return input_string
def start(file, strength):
    
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
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]


    # # Create an instance of ChessArrayComparator
    comparator = ChessArrayComparator(initial_array)

    # # Check the initial array once
    move = comparator.compare_and_update(found)
    strings_to_exclude = ["from array 0", "from array 1"]


    result = parse_strings(move, strings_to_exclude)
    result = result.replace('\n', '')

    # # If the initial array is checked and some pieces are moved, update the initial array
    if move:
        initial_array = found
    # Save the updated initial array using pickle
        with open('initial_array.pkl', 'wb') as initial_file:
            pickle.dump(initial_array, initial_file)
    chessai = chessmove(result, strength)
    print(chessai)
    end = time.time()
    print("It took " + str(end - start) + " to finish. " + "The output saved in " + output_folder + " moves that occurred " + result)
    return chessai
