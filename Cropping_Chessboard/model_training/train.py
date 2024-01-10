from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.train(data="/Users/akash/Source/chessAI/Chessboard_Recognition/Chessboardseg/data.yaml", epochs=50,  imgsz=640, batch =-1) # add device device='mps for apple silicon devices and remove batch=-1 on apple silicon 
metrics = model.val()
results = model("/Users/akash/Source/chessAI/Chessboard_Recognition/images/Chessboard2.jpg", save=True)
model.export(format='onnx')

