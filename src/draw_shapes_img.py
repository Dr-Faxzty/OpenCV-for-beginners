import numpy as np
import cv2


img = cv2.imread("/home/dr_faxzty/Desktop/scuola/PON ecc/Rescue Line/2024/OpenCV-for-beginners/src/assets/img/HappyFish.jpg", 1)

#create img with numpy
img =  np.zeros([312, 312, 3], np.uint8) # it creates a black image with 312x312 pixels and 3 channels (BGR)
# np.zeros([height, width, channels], data_type) 
# -> channels = 3 (BGR) or 1 (grayscale) or 2 (grayscale + alpha channel) or 4 (BGR + alpha channel)
# -> data_type = np.uint8 (unsigned integer 8 bit) -> 0 = black, 255 = white

scale_percent = 200
x = width = int(img.shape[1] * scale_percent / 100)
y = height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)


# draw a line on the image
start_point = (0, 0)
end_point = (x, y)
color = (0, 255, 0)
thickness = 5

img = cv2.line(img, start_point, end_point, color, thickness)
# (image, start_point, end_point, color, thickness) 
# -> start_point = (x, y) -> end_point = (x, y) -> color = (B, G, R) -> thickness = line thickness in pixels

# draw arrowed line on the image
img = cv2.arrowedLine(img, (0, y // 2), (x // 2, y // 2), (255, 0, 0), 5)
# (image, start_point, end_point, color, thickness) 
# -> start_point = (x, y) -> end_point = (x, y) -> color = (B, G, R) -> thickness = line thickness in pixels

# draw rectangle on the image
img = cv2.rectangle(img, (x // 2, 0), (x, y // 2), (0, 0, 255), cv2.FILLED)
# (image, start_point, end_point, color, thickness) 
# -> start_point = (x, y) -> end_point = (x, y) -> color = (B, G, R) -> thickness = line thickness in pixels
# if you want to fill the rectangle, you have to use cv2.FILLED as thickness or -1
'''
x1,y1 ------
|          |
|          |
|          |
--------x2,y2
'''


# draw a circle on the image
center = (x // 2, y // 2)
radius = 100

img = cv2.circle(img, center, radius, (255, 255, 0), 5)
# (image, center, radius, color, thickness) 
# -> center = (x, y) -> radius = int -> color = (B, G, R) -> thickness = line thickness in pixels


# draw a text on the image
text = "Happy Fish"
start_point = (x // 2 - 75, y - 50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0, 255, 255)
thickness = 2
line_type = cv2.LINE_AA # cv2.LINE_AA = antialiased line -- cv2.LINE_4 = 4-connected line -- cv2.LINE_8 = 8-connected line

img = cv2.putText(img, text, start_point, font, font_scale, color, thickness, line_type)

cv2.imshow("Image", img)


key = cv2.waitKey(0)

if key == 27 or key == ord("q"):
    cv2.destroyAllWindows()