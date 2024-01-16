# chessboard

- The finding_squares folder contains methods to find which square is which. 
- The model_training folder contains training code for the chessboard cropping algorithm using Yolov8
- The finished_training folder contains the trained chessboard cropping with weights for the Yolov8 Model
- roboflow_api contains the chessboard cropping algorith using the Roboflow's api 
- repostory for the training dataset for the chessboard cropping: https://universe.roboflow.com/steven-lt9bf/chessboard-segmentation


## Code that is mostly production ready
- check the final_algorithm which contains a start.py file and modify the parmeters with your desire path for the image and run the code 

## Code that is currently working that you can try : 
- predict.py in finished_training works with a given image path it will crop to the chessboard and output cropped.png
- intersectionvthree.py contains the code to find the intersections
- box.py finds the intersection and groups them into boxs with the labels of chess coordinates
- boxout.py does exactly what box.py does except it outputs each Individual square as it's own image with coordinates
## Recommendation on how to run on other machines:
1. install annaconda or miniconda(smaller verison)

2. Run the follwing commands in the directory with environment.yaml
 
   1. run  ```conda config --append channels conda-forge```
   2. run ```conda env create -f environment.yml```
   3. run this command every time you open a new shell```conda activate chesstorch``` 
3. Run any of the code that is listed under currently working

