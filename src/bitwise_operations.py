import cv2
import numpy as np


img1 = np.zeros((500, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

img2 = np.zeros((500, 500, 3), np.uint8)
img2 = cv2.rectangle(img2, (250, 0), (500, 500), (255, 255, 255), -1)


# bitwise operations are useful when working with masks: binary images with 0s and 1s only (black and white) which are used to select regions of interest
# bitwise AND, OR, XOR, NOT

bit_and = cv2.bitwise_and(img1, img2)
# (img1, img2, dst, mask = None) -> dst = img1 & img2 (if mask is None) else dst = img1 & img2 & mask
# bitwise AND: if both pixels are greater than 0, then the pixel is turned on (1) else it is turned off (0)


bit_or = cv2.bitwise_or(img1, img2)
# bitwise OR: if either of the two pixels are greater than 0, then the pixel is turned on (1) else it is turned off (0)


bit_xor = cv2.bitwise_xor(img1, img2)
# bitwise XOR: if either of the two pixels are greater than 0, but not both, then the pixel is turned on (1) else it is turned off (0)
# bitwise XOR is useful for selecting regions of an image that are different from a second image


bit_not1 = cv2.bitwise_not(img1)
# bitwise NOT: inverts the "on" and "off" pixels in an image
# bitwise NOT is useful for selecting regions of an image that are similar to a second image

bit_not2 = cv2.bitwise_not(img2)
# bitwise NOT: inverts the "on" and "off" pixels in an image


# funny trick: bitwise NOT is the same as subtracting the image from a matrix of ones
bit_not1 = 255 - img1

# funny trick: bitwise OR
bit_or = img1 | img2
# this is because the maximum value of a pixel is 255, so if both pixels are 255, then the result is 255 (1) else it is 0 (0)

# funny trick: bitwise AND
bit_and = img1 & img2
# this is because the minimum value of a pixel is 0, so if both pixels are 0, then the result is 0 (0) else it is 255 (1)

# funny trick: bitwise XOR
bit_xor = (img1 | img2) - (img1 & img2)
# by definition, bitwise XOR is the same as bitwise OR minus bitwise AND


# funny trick: de Morgan's laws 
# not (A and B) = not A or not B
# not (A or B) = not A and not B

# bitwise NOT of bitwise AND is the same as bitwise OR of bitwise NOTs
bit_not_and = cv2.bitwise_not(img1 & img2)
bit_or_not = cv2.bitwise_or(cv2.bitwise_not(img1), cv2.bitwise_not(img2))

# bitwise NOT of bitwise OR is the same as bitwise AND of bitwise NOTs
bit_not_or = cv2.bitwise_not(img1 | img2)
bit_and_not = cv2.bitwise_and(cv2.bitwise_not(img1), cv2.bitwise_not(img2))



cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

cv2.imshow("bit_and", bit_and)
cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_xor", bit_xor)
cv2.imshow("bit_not1", bit_not1)
cv2.imshow("bit_not2", bit_not2)
cv2.imshow("bit_not_and", bit_not_and)
cv2.imshow("bit_or_not", bit_or_not)
cv2.imshow("bit_not_or", bit_not_or)
cv2.imshow("bit_and_not", bit_and_not)




key = cv2.waitKey(0) & 0xFF

if key == 27 or key == ord("q"):
    cv2.destroyAllWindows()