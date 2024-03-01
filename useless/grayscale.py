import cv2    

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
    return division
    # cv2.imshow('division', division)  
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()