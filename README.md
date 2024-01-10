# chessboard

- The finding_squares folder contains methods to find which square is which. 
- The model_training folder contains training code for the chessboard cropping algorithm using Yolov8
- The finished_training folder contains the trained chessboard cropping with weights for the Yolov8 Model
- roboflow_api contains the chessboard cropping algorith using the Roboflow's api 
- repostory for the training dataset for the chessboard cropping: https://universe.roboflow.com/steven-lt9bf/chessboard-segmentation


## Code that is currently working that you can try: 
- predict.py in finished_training works with a given image path it will crop to the chessboard and output cropped.png
- intersectionvthree.py contains the code to find the intersections
- box.py and finds the intersection and groups them into boxs with the labels of chess cordinates

## Recommendation on how to run on other machines:
1. install annaconda or miniconda(smaller verison)

2. Run the follwing command in the directory with environment.yaml
 ```conda env create -f environment.yml```

3. Run any of the code that is listed under currently working
