from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('best.onnx')

# Define path to the image file
source = '/Users/akash/Source/chessAI/Chessboard_Recognition/images/Chessboard2.jpg'

# Run inference on the source
results = model(source, save=True)  # list of Results objects