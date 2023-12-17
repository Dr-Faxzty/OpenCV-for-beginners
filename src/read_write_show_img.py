import cv2
import numpy as np

# read image
img = cv2.imread("src/assets/orso.png", 1) # 0 = grayscale = cv2.IMREAD_GRAYSCALE -- 1 = color = cv2.IMREAD_COLOR -- -1 = unchanged = cv2.IMREAD_UNCHANGED -> include alpha channel
# color channels: BGR (Blue, Green, Red) -> OpenCV uses BGR format instead of RGB format because it was developed by Intel and they used BGR format for their cameras

# to convert BGR to RGB format -> good practice
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# why BGR format? -> https://learnopencv.com/why-does-opencv-use-bgr-color-format/


#print(img) # print image as matrix of pixels (0-255) -> 0 = black, 255 = white

# write image
#cv2.imwrite("src/assets/orso_copy.png", img)  
# write image to file (path, image) -> image must be in BGR format (not RGB) -> if you want to save it in RGB format, you have to convert it first


# show image
cv2.imshow('Happy Orso', img)

# wait for key press to close window (0 = infinite time -- 1000 = 1 second -- 5000 = 5 seconds)
cv2.waitKey(0)
# its a good practice to use & 0xFF with waitKey() because of 64-bit machines (it will return 32-bit int instead of 8-bit) -> 0xFF = 11111111 in binary


# wait for key press to close window (27 = ESC key) or s to save a copy (ord('s') = s key)
'''
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite("src/assets/orso_copy_2.png", img)
    cv2.destroyAllWindows()
'''

# destroy all windows
cv2.destroyAllWindows()

# destroy specific window
#cv2.destroyWindow('Happy Panda')