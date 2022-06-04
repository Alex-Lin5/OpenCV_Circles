import numpy as np
import cv2

# read a image from local directory, and turn it into
# gray scale image, using median filter to have a blurred image
img = cv2.imread('bubbles-g58607190e_1920.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray, 25) 

# PARAMETER OF HOUGHCIRCLES
# minimum distance between circles
minDist = 70
# the smaller value, the more false circles around the correct one
param1 = 10 
param2 = 33 
# the min and max radius of circle
minRadius = 7
maxRadius = 90

# HoughCircles function is used to detect circles
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist,
    param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

# draw circles detected on the image
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)

# Show result for parameter adjusting
cv2.imshow('imgout', img)
cv2.waitKey(0)

'''
acknowledge code from Stackoverflow@Toriam
https://stackoverflow.com/questions/60637120/detect-circles-in-opencv

cv2.circle()
https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670
void cv::circle	(
InputOutputArray 	img,
Point 	center,
int 	radius,
const Scalar & 	color,
int 	thickness = 1
)

cv2.medianBlur()
https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga564869aa33e58769b4469101aac458f9

cv2.HoughCircles()
https://docs.opencv.org/3.4/d3/de5/tutorial_js_houghcircles.html

'''