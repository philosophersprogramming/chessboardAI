import cv2
import numpy as np

# Load image, grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread("detect.png")
mask = np.zeros(image.shape, dtype=np.uint8)
original = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Remove noise with morph operations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening

# Find contours and find squares with contour area filtering + shape approximation
cnts = cv2.findContours(invert, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv2.contourArea(c)
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4 and area > 100 and area < 10000:
        x,y,w,h = cv2.boundingRect(c)
        cv2.drawContours(original, [c], -1, (36,255,12), 2)
        cv2.drawContours(mask, [c], -1, (255,255,255), -1)

cv2.imshow("original", original)
cv2.imshow("mask", mask)
cv2.waitKey()

