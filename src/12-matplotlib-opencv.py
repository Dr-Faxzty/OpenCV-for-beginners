import cv2
import numpy as np
import matplotlib.pyplot as plt

#img = cv2.imread('/home/drfaxzty/Documents/PROJECTS/OpenCV-for-beginners/src/assets/img/lena.jpg', -1)

img = cv2.imread('/home/drfaxzty/Documents/PROJECTS/OpenCV-for-beginners/src/assets/img/gradient.png', 0)

cv2.imshow('image', img)

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # This will convert the image from BGR to RGB
# in order to show the image correctly in matplotlib

#plt.imshow(img) # This will show the image in a matplotlib window
#plt.xticks([]), plt.yticks([]) # This will remove the x and y axis

_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i + 1) # This will create a 2x3 grid of images and will show the image in the i + 1 position of the grid
    plt.imshow(images[i], 'gray')
    plt.title(titles[i]) # This will set the title of the image
    plt.xticks([]), plt.yticks([]) # This will remove the x and y axis




plt.show() # This will show the matplotlib window

cv2.waitKey(0)
cv2.destroyAllWindows()