import cv2 as cv
import numpy as np


# threshold is a very popular segmentation technique used for separating an object from its background
# the process of thresholding involves comparing each pixel of an image with a predefined threshold value
# this type of comparison of each pixel of a image to a threshold value divide all the pixel into two groups
# the first group contains the pixel values that are less than the threshold value and the second group contains the pixel values that are greater than the threshold value


img = cv.imread("assets/img/gradient.png", 0)


# this method returns two values, the first value is the threshold value and the second value is the thresholded image
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY) # if the pixel value is greater than the threshold value, it is assigned one value (white), else it is assigned another value (black)
# cv.THRESH_BINARY is the type of thresholding technique used here
# 127 is the threshold value
# 255 is the maximum value that can be assigned to a pixel

# if the pixel value is greater than the threshold value, it is assigned another value (black), else it is assigned one value (white)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV) 

# if the pixel value is greater than the threshold value, it is assigned the threshold value, else it is assigned the original value
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

# if the pixel value is greater than the threshold value, it is assigned the original value, else it is assigned zero
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

# if the pixel value is greater than the threshold value, it is assigned zero, else it is assigned the original value
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)

cv.waitKey(0)
cv.destroyAllWindows()