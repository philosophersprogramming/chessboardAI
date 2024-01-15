from ultralytics import YOLO
import numpy as np
import cv2
import json

# Load a pretrained YOLOv8n model
model = YOLO('weights/best.pt')

# Define path to the image file
source = '/Users/akash/Source/chessAI/Chessboard_Recognition/Finding_pieces/AI_detection/Training_dataset/Black-Pieces/board5e1.png'

# Run inference on the source
results = model(source)  # list of Results objects

