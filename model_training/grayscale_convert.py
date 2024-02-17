import cv2    
import os


# File created for lazy Akash who doesn't want to write loops.
def grayscaleImg(img_path, out_path):    
    # read the image
    img = cv2.imread(img_path)

    # convert to gray
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # blur
    smooth = cv2.GaussianBlur(gray, (95,95), 0)

    # divide gray by morphology image
    division = cv2.divide(gray, smooth, scale=192)

    # save results
    cv2.imwrite(out_path, division)
    # cv2.imshow('division', division)  
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
def grayscale_folder(path, outpath):
    image_files = [f for f in os.listdir(path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    for image_file in image_files:
        print(f"{path}/{image_file}")
        grayscaleImg(f"{path}/{image_file}", f"{outpath}/{image_file}")

if __name__ == "__main__":
    grayscale_folder("../images", "images")
