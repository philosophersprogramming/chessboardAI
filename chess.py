from roboflow import Roboflow

rf = Roboflow(api_key=" ")
project = rf.workspace().project("chessboard-segmentation")
model = project.version(1).model

# infer on an image hosted elsewhere
print(model.predict("Chessboard.jpg").json())

# save an image annotated with your predictions
model.predict("Chessboard.jpg").save("prediction.jpg")


