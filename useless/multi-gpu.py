from ultralytics import YOLO
import os
import time
from multiprocessing import Pool, freeze_support, set_start_method
import tensorrt

print(tensorrt.__version__)
assert tensorrt.Builder(tensorrt.Logger())

model = YOLO('weights/piece/best.engine', task='classify')

def process_batch(batch, directory_path):
    image_files, row_col_info = batch
    pieces_array = [[None for _ in range(8)] for _ in range(8)]  # Initialize pieces_array as a regular list
    for (image_file, (row, col)) in zip(image_files, row_col_info):
        source = os.path.join(directory_path, image_file)
        results = model(source)
        probs = results[0].probs.top1
        if probs == 0:
            pieces_array[7 - row][col] = 2
        elif probs == 2:
            pieces_array[7 - row][col] = 1
        elif probs == 1:
            pieces_array[7 - row][col] = 0
    return pieces_array

def pieces(path, batch_size=4):
    start = time.time()
    directory_path = path
    image_files = [f for f in os.listdir(directory_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

    # Divide image files into batches
    batches = [(image_files[i:i+batch_size], [extract_row_col_from_filename(f) for f in image_files[i:i+batch_size]])
               for i in range(0, len(image_files), batch_size)]

    # Create a multiprocessing pool
    with Pool() as pool:
        results = pool.starmap(process_batch, [(batch, directory_path) for batch in batches])

    # Combine results from all batches
    combined_pieces_array = [[None for _ in range(8)] for _ in range(8)]
    for result in results:
        for i in range(8):
            for j in range(8):
                if combined_pieces_array[i][j] is None:
                    combined_pieces_array[i][j] = result[i][j]

    print("Pieces Array:")
    for row in combined_pieces_array:
        print(row)

    end = time.time()
    print("It took", end - start, "seconds")
    return combined_pieces_array

def extract_row_col_from_filename(filename):
    col = ord(filename[0].lower()) - ord('a')
    row = int(filename[1]) - 1
    return row, col

if __name__ == '__main__':
    set_start_method('spawn')
    freeze_support()
    pieces('out')
