from ultralytics import YOLO
import os
import tensorrt

print(tensorrt.__version__)
assert tensorrt.Builder(tensorrt.Logger())

model = YOLO('weights/piece/best.engine', task='classify')
def pieces(path):
# Load a pretrained YOLOv8n model
    

# Define path to the directory containing image files
    directory_path = path

    image_files = [f for f in os.listdir(directory_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
# Initialize an empty 2D array for pieces
    pieces_array = [['' for _ in range(8)] for _ in range(8)]

    counterblack = 0
    counterwhite = 0
    # Iterate over each image file
    for image_file in image_files:
            # Construct the full path to the image file
            source = os.path.join(directory_path, image_file)

            # Run inference on the source
            results = model(source)  # list of Results objects, don't include  device='mps' if not apple silicon device
            # Ensure results is a list and not None
            probs = results[0].probs.top1
            names = results[0].names
            row, col = extract_row_col_from_filename(image_file)
            print (str(probs) + str(names))
            if (probs == 0) :
                print("black")
                pieces_array[row][col] = 2
                counterblack+=1
            if (probs == 2) :
                print("white")
                pieces_array[row][col] = 1
                counterwhite+= 1
            if (probs == 1) :
                 pieces_array[row][col] = 0
                 print("blank square")
    print("Pieces Array:")
    for row in pieces_array:
        print(row)
    
    return "found " + str(counterblack) + " black pieces and found " + str(counterwhite) + " white pieces"
   
def extract_row_col_from_filename(filename):
    # Extracts row and column information from the chess position in the filename

    # Assuming the filename is in the format "<column><row>.<extension>"
    # For example, "a4.jpg", "b4.png"

    # Extract column from the first character of the filename
    col = ord(filename[0].lower()) - ord('a')

    # Extract row from the second character of the filename
    row = int(filename[1]) - 1

    return row, col

