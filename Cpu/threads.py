from ultralytics import YOLO
import os
from threading import Thread
import time

def thread_safe_predict(image_path, pieces_array):
    # Instantiate a new model inside the thread
    local_model = YOLO("weights/pieces/v6/best.pt")
    results = local_model.predict(image_path)
    # Process results
    probs = results[0].probs.top1
    row, col = extract_row_col_from_filename(os.path.basename(image_path))
    

    if probs == 0:
        print("black")
        pieces_array[7 - row][col] = 2
    elif probs == 2:
        print("white")
        pieces_array[7 - row][col] = 1 
    elif probs == 1:
        print("blank square")
        pieces_array[7 - row][col] = 0 
            

def pieces(path):
    start = time.time()
    # Define path to the directory containing image files
    directory_path = path

    image_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    # Initialize an empty 2D array for pieces
    pieces_array = [['' for _ in range(8)] for _ in range(8)]

    threads = []

    # Iterate over each image file
    for image_file in image_files:

        # Starting threads that each have their own model instance
        thread = Thread(target=thread_safe_predict, args=(image_file, pieces_array))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("Pieces Array:")
    for row in pieces_array:
        print(row)
    end = time.time()
    print("It took" + str(end - start))
    return pieces_array


def extract_row_col_from_filename(filename):
    # Extracts row and column information from the chess position in the filename

    # Assuming the filename is in the format "<column><row>.<extension>"
    # For example, "a4.jpg", "b4.png"

    # Extract column from the first character of the filename
    col = ord(filename[0].lower()) - ord('a')

    # Extract row from the second character of the filename
    row = int(filename[1]) - 1

    return row, col

pieces('out')
