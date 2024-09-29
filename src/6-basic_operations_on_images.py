import numpy as np
import cv2


img = cv2.imread("assets/img/lena.jpg", 1)
img2 = cv2.imread("assets/img/HappyFish.jpg", 1)


print(img.shape) # return a tuple of number of rows, columns and channels
print(img.size) # return total number of pixels is accessed
print(img.dtype) # return image datatype is obtained (very useful for debugging)

b, g, r = cv2.split(img) # split image into its three channels

img = cv2.merge((b, g, r)) # merge the three channels into one image

# ROI: Region of Interest
# sometimes we need to work with a certain region of the image

eye = img[240:300, 240:300] # get the region of the eye with numpy slicing (y, x) or (column, rows) or (height, width)
img[273:333, 100:160] = eye # copy the eye region into another region


# rotate image
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # rotate clockwise
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # rotate counterclockwise
img = cv2.rotate(img, cv2.ROTATE_180) # rotate 180 degrees
# (image, rotateCode) -> rotateCode = flag that takes 3 values (ROTATE_90_CLOCKWISE, ROTATE_90_COUNTERCLOCKWISE, ROTATE_180)


# resize image
scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
# (image, dsize, fx[optional], fy[optional], interpolation[optional]) -> dsize = desired size (width, height) 
# -> fx = scale factor along the horizontal axis -> fy = scale factor along the vertical axis 
# -> interpolation = interpolation method used to resize the image (INTER_AREA = good for shrinking, INTER_CUBIC = good for zooming)


img = cv2.resize(img, (512, 512)) # resize image to 512x512
img2 = cv2.resize(img2, (512, 512)) # resize image to 512x512

# add two images 
dst = cv2.add(img, img2) # calculate the sum of two images or an array and a scalar
# to make the sum of two images we need to make sure that the two images have the same size and same number of channels. So, resize the images first


# add two images with different weights
dst = cv2.addWeighted(img, 0.9, img2, 0.1, 0) # calculate the weighted sum of two images or an image and an array
# (src1, alpha, src2, beta, gamma) -> alpha = weight of the first array elements -> beta = weight of the second array elements -> gamma = scalar added to each sum


cv2.imshow('image', dst)

key = cv2.waitKey(0) & 0xFF

if key == 27 or key == ord("q"):
    cv2.destroyAllWindows()