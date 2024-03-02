from ultralytics import YOLO

model = YOLO('/home/akash/chessboard/Cpu/weights/pieces/v6/best.pt')

model.export(format='engine')

