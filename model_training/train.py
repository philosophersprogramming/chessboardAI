from ultralytics import YOLO
import comet_ml

comet_ml.init(project_name="chessboardai")
model = YOLO('yolov8n-cls.pt')
results = model.train(data="/Users/akash/Source/chessAI/train-dataset", epochs=50, imgsz=640, device='mps', project="chessboardai", save_period=1,
save_json=True)

