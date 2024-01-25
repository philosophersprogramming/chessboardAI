from ultralytics import YOLO

model = YOLO('/home/akash/chessboard/Finding_pieces/AI_detection/weightsv2/best.pt')

model.export(format='engine')

