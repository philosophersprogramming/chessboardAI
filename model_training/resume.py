from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO('weights/last copy.pt')
    results = model.train(resume=True, data="dataset2", epochs=300, imgsz=640, project="chessboardai", save_period=1, batch=8, save_json=True)
