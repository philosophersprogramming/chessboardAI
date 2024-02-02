from ultralytics import YOLO

model = YOLO('/home/akash/chessboard/new-algorithm/Not-optimized/weights/pieces/best.pt')

model.export(format='engine')

