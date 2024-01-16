from ultralytics import YOLO
import os

model = YOLO('weights/pieces/best.pt')
def pieces(path):
# Load a pretrained YOLOv8n model
    

# Define path to the directory containing image files
    directory_path = path

    image_files = [f for f in os.listdir(directory_path) if f.endswith(('.png', '.jpg', '.jpeg'))]


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
            print (str(probs) + str(names))
            if (probs == 0) :
                print("black")
                counterblack+=1
            if (probs == 2) :
                print("white")
                counterwhite+= 1
            if (probs == 1) :
                 print("blank square")
    print("found " + str(counterblack) + " black pieces and found " + str(counterwhite) + " white pieces")

        