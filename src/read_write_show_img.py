import cv2

# read image
img = cv2.imread("src/assets/img/orso.png", 1) # 0 = grayscale = cv2.IMREAD_GRAYSCALE -- 1 = color = cv2.IMREAD_COLOR -- -1 = unchanged = cv2.IMREAD_UNCHANGED -> include alpha channel
# color channels: BGR (Blue, Green, Red) -> OpenCV uses BGR format instead of RGB format because it was developed by Intel and they used BGR format for their cameras

# to convert BGR to RGB format -> good practice
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# why BGR format? -> https://learnopencv.com/why-does-opencv-use-bgr-color-format/


#print(img) # print image as matrix of pixels (0-255) -> 0 = black, 255 = white

# write image
cv2.imwrite("assets/saved_frames/orso_copy.png", img)  
# write image to file (path, image) -> image is in BGR format (not RGB) -> if you want to save it in RGB format, you have to convert it first


# resize image
scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
# (image, dsize, fx[optional], fy[optional], interpolation[optional]) -> dsize = desired size (width, height) 
# -> fx = scale factor along the horizontal axis -> fy = scale factor along the vertical axis 
# -> interpolation = interpolation method used to resize the image (INTER_AREA = good for shrinking, INTER_CUBIC = good for zooming)


# rotate image
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # rotate clockwise
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # rotate counterclockwise
img = cv2.rotate(img, cv2.ROTATE_180) # rotate 180 degrees
# (image, rotateCode) -> rotateCode = flag that takes 3 values (ROTATE_90_CLOCKWISE, ROTATE_90_COUNTERCLOCKWISE, ROTATE_180)

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
    cv2.imwrite("src/assets/saved_frames/orso_copy_2.png", img)
    cv2.destroyAllWindows()
'''

# destroy all windows
cv2.destroyAllWindows()

# destroy specific window
#cv2.destroyWindow('Happy Panda')
