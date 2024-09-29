import cv2 as cv
import numpy as np


# Adaptive thresholding is the method where the threshold value is calculated for smaller regions and therefore,
# there will be different threshold values for different regions and not for every pixel in the image

# Why do we need this type of thresholding?
# In some cases, the image may contain different lighting conditions in different regions and therefore,
# the same threshold value may not be suitable for all the regions in the image
# So this method is used to overcome this problem and to get better results


img = cv.imread("/home/drfaxzty/Documents/PROJECTS/OpenCV-for-beginners/src/assets/img/sudoku.png", 0)

# If we show the image, we can see that the image contains different lighting conditions in different regions
# and we will see half of the image is bright and the other half is dark
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# cv.ADAPTIVE_THRESH_MEAN_C is the type of adaptive thresholding technique used here
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
# 255 is the maximum value that can be assigned to a pixel
# cv.ADAPTIVE_THRESH_MEAN_C is the type of adaptive thresholding technique used here -> the threshold value is the mean of the neighbourhood area minus the constant value
# 11 is the size of the neighbourhood area
# 2 is the constant value that is subtracted from the mean of the neighbourhood area

# cv.ADAPTIVE_THRESH_GAUSSIAN_C is the type of adaptive thresholding technique used here
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# 255 is the maximum value that can be assigned to a pixel
# cv.ADAPTIVE_THRESH_GAUSSIAN_C is the type of adaptive thresholding technique used here -> the threshold value is the weighted sum of the neighbourhood values where weights are a gaussian window
# 11 is the size of the neighbourhood area
# 2 is the constant value that, in this case, is the weighted sum of the neighbourhood values


cv.imshow("Image", img)
cv.imshow("Threshold", th1)
cv.imshow("Adaptive Threshold Mean", th2)
cv.imshow("Adaptive Threshold Gaussian", th3)

cv.waitKey(0)
cv.destroyAllWindows()