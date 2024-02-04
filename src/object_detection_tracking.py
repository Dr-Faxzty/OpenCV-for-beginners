# HSV = Hue Saturation Value

# Hue: 0-360
# Corresponds to the color components (base pigments), hence just by selecting a range of Hue you can select any color
# e.g. If you want to detect only red color then select Hue values of 0-100 (approx) and if you want to detect green color then select Hue values of 100-180.

# Saturation: 0-100%
# Is the amount of color (depth of the pigment) (dominance of Hue) (0% means no color (gray scale image) and 100% means full color)
# e.g. Red color with 100% saturation will be pure red. But if we reduce the saturation level to 50% then the red color will become pink (less red).  

# Value: 0-100%
#Is basically the brightness of the color.


# Generally RGB color space are correlated to the color luminance.
# We cannot separate the color information from the luminance information

# HSV is used to separate image luminance from the color informations. 
# So, makes it easier when we need luminance information for image processing tasks like object tracking and detection


# In OpenCV, the range for HSV is H: 0-179, S: 0-255, V: 0-255 


import cv2
import numpy as np

def nothing(x):
    pass


#cap = cv2.VideoCapture(0)


# The trackbar is useful to change the value of the threshold dynamically during the runtime
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing) # LH = Lower Hue
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing) # LS = Lower Saturation
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing) # LV = Lower Value

cv2.createTrackbar("UH", "Tracking", 255, 255, nothing) # UH = Upper Hue
cv2.createTrackbar("US", "Tracking", 255, 255, nothing) # US = Upper Saturation
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing) # UV = Upper Value


while True:
    frame = cv2.imread("/home/dr_faxzty/Desktop/scuola/PON ecc/Rescue Line/2024/OpenCV-for-beginners/src/assets/img/smarties.png")
    #_, frame = cap.read()
    
    # Let's say we want to detect only the blue color in the image
    
    # For that we need to convert the image to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Now we need to define the range of a color in HSV dynamically using the trackbar
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")
    
    
    # Now we need to define the range of the color in HSV
    l_b = np.array([l_h, l_s, l_v]) # lower bound of color -> means the minimum value of color in HSV color space
    u_b = np.array([u_h, u_s, u_v]) # upper bound of color -> means the maximum value of color in HSV color space
    
    
    # Now we have to threshold the HSV image to get only the colors within the range
    # thresholding is the process of converting an image to a binary image (black and white image)
    mask = cv2.inRange(hsv, l_b, u_b) # mask is the thresholded image of the original image which contains only the needed color
    
    # Now we need to bitwise AND the original image and the mask
    res = cv2.bitwise_and(frame, frame, mask=mask) # res is the image which contains only the needed color
    
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    
    
    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        break
    
#cap.release()
cv2.destroyAllWindows()