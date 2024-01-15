from ultralytics import YOLO

model = YOLO('yolov8n-cls.pt')
model.train(data="", epochs=50, batch=-1, imgsz=640)
# get dataset from https://universe.roboflow.com/chessboard-a6qsc/chess_pieces-8sifu/dataset/1
metrics = model.val()
metrics.top1 # top1 accuracy
metrics.top5 # top5 accuracy
model.export(format='onnx')