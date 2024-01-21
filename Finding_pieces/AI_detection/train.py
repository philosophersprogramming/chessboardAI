from ultralytics import YOLO

model = YOLO('yolov8n-cls.pt')
model.train(data="LOCATION TO MODEL", epochs=10, batch=-1, imgsz=640)
metrics = model.val()
metrics.top1 # top1 accuracy
metrics.top5 # top5 accuracy
