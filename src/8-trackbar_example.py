import numpy as np
import cv2


def nothing(x):
    print(x)


img = np.zeros((300, 512, 3), np.uint8)
img2 = cv2.imread("assets/img/lena.jpg")
cv2.namedWindow('color')
cv2.namedWindow('gray')

# trackbars are very useful to change the value of certain parameters during runtime

# (trackbar name, window name, min value, max value, callback function) -> callback function is called everytime the trackbar value is changed
cv2.createTrackbar('B', 'color', 0, 255, nothing)
cv2.createTrackbar('G', 'color', 0, 255, nothing)
cv2.createTrackbar('R', 'color', 0, 255, nothing)

cv2.createTrackbar('CP', 'gray', 10, 400, nothing) # CP - current position

switchCP = 'Color/Gray'
cv2.createTrackbar(switchCP, 'gray', 0, 1, nothing)

switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'color', 0, 1, nothing)


while True:
    img2 = cv2.imread("assets/img/lena.jpg")
    
    cv2.imshow('color', img)
    
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break
    
    # get the current position of the trackbar
    b = cv2.getTrackbarPos('B', 'color') # (trackbar name, window name)
    g = cv2.getTrackbarPos('G', 'color')
    r = cv2.getTrackbarPos('R', 'color')
    s = cv2.getTrackbarPos(switch, 'color')
    
    # write the current position of the trackbar on the image
    pos = cv2.getTrackbarPos('CP', 'gray')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img2, str(pos), (50, 150), font, 4, (255, 255, 255), 10)
    
    s_cp = cv2.getTrackbarPos(switchCP, 'gray')
    
    # set the image to the current trackbar values
    if s == 0:
        img[:] = 0
    else: 
        img[:] = [b, g, r]
    
    # convert the image to grayscale if the switch is on
    if s_cp == 0:
        pass
    else:
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('gray', img2)
    
    
cv2.destroyAllWindows()