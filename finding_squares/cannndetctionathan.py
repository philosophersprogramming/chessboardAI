import sys
import math
import cv2
import numpy as np
from collections import defaultdict


def main(argv):
    filename = '/Users/akash/Source/chessAI/Chessboard_Recognition/finished_training/cropped.png'
    
    # Loads an image
    src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_GRAYSCALE)
    src = cv2.resize(src, (0, 0), fx=0.75, fy=0.75)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_lines.py [image_name -- default ' + filename + '] \n')
        return -1
    
    # Canny Edge Transformation
    dst = cv2.Canny(src, 50, 160, None, 3)
    
    # Copy edges to the images that will display the results in BGR
    cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)    
    lines = cv2.HoughLines(dst, 1, np.pi / 180, 160, None, 0, 0)
    
    segmented = segment_by_angle_kmeans(lines)
    if segmented is not None:
        for i in range(0, len(segmented)):
            for j in range(0, len(segmented[i])):
                rho = segmented[i][j][0][0]
                theta = segmented[i][j][0][1]

                a = math.cos(theta)
                b = math.sin(theta)

                x0 = a * rho
                y0 = b * rho    

                pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
                pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
                cv2.line(cdst, pt1, pt2, (0,255 * i,255), 1, cv2.LINE_AA)
    
    intersections = []
    for line1 in segmented[0]:
        for line2 in segmented[1]:
            intersections.append(get_intersection(line1, line2))
    
    # ordered_intersections = {}
    # for intersection in intersections:
    #     print(intersection)
    #     x = intersection[0][0]
    #     y = intersection[0][1]
        
    #     xheat = math.floor((x / 1000) * 10)
    #     yheat = math.floor((y / 1000) * 10)

    #     dot = xheat + yheat
    #     if not dot in ordered_intersections.keys():
    #      ordered_intersections[dot] = []
    #     cv2.circle(cdst, intersection[0], 8, (25 * dot, 25 * dot, 255), 1)
    arr = np.array(intersections, dtype=np.float32)
    print(intersections)
    criteria = ((cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER), 10, 1.0)
    attempts = 10
    flags = cv2.KMEANS_RANDOM_CENTERS

    _, _, centers = cv2.kmeans(arr, 81, None, criteria, attempts, flags)
    centers = sort_intersections(centers)
    
    # show the centers/intersections of the board
    for row in centers:
        for center in row:
            print(center)
            cv2.circle(cdst, (int(center[0]), int(center[1])), 9, (255, 255, 0), 1)
    
    
    # store each tile into the out folder.
    for i in range(8):
        for j in range(8):
            x1, y1 = centers[i][j]
            x2, y2 = centers[i][j + 1]
            x3, y3 = centers[i + 1][j]
            x4, y4 = centers[i + 1][j + 1]
            
            top_left_x = int(min([x1,x2,x3,x4]))
            top_left_y = int(min([y1,y2,y3,y4]))
            bot_right_x = int(max([x1,x2,x3,x4]))
            bot_right_y = int(max([y1,y2,y3,y4]))
            
            cv2.imwrite(f"out/{j * 8 + i}.jpg", cdst[top_left_y:bot_right_y + 1, top_left_x:bot_right_x + 1])
            


    cv2.imshow("Source", src)
    cv2.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    
    cv2.waitKey(0)
    return 0


# This function will separate the array of lines to vertical and horizontal lines.
def segment_by_angle_kmeans(lines):
    # just the settings for the function
    criteria = ((cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER), 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    attempts = 10

    # return angles [0, pi] in radians
    angles = np.array([line[0][1] for line in lines], dtype=np.float32)
    pts = np.array([[np.cos(2 * angle), np.sin(2 * angle)] for angle in angles], dtype=np.float32)
    _, labels, center = cv2.kmeans(pts, 2, None, criteria, attempts, flags)
    labels = labels.reshape(-1)
    # print(labels)
    # print(center)
    
    segmented = defaultdict(list)
    for k, line in enumerate(lines):
        segmented[labels[k]].append(line)
    segmented = list(segmented.values())
    return segmented
    
def sort_intersections(centers):
    centers = centers[centers[:, 0].argsort()]
    centers = centers.reshape(9, 9, 2)
    
    for i in range(len(centers)):
        row = centers[i]
        centers[i] = row[row[:, 1].argsort()]
    return centers
    
def get_intersection(line1, line2):
    rho1, theta1 = line1[0]
    rho2, theta2 = line2[0]
    A = np.array([
        [np.cos(theta1), np.sin(theta1)],
        [np.cos(theta2), np.sin(theta2)]
    ])
    b = np.array([[rho1], [rho2]])
    x0, y0 = np.linalg.solve(A, b)
    x0, y0 = int(np.round(x0)), int(np.round(y0))
    return [[x0, y0]]
    
if __name__ == "__main__":
    main(sys.argv[1:])