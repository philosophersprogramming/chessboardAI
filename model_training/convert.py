from ultralytics import YOLO

model = YOLO('/home/akash/chessboard/final_algorithm/Not-optimized/weights/pieces/v4/best.pt')

model.export(format='engine')

