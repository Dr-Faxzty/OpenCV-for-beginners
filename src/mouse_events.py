import numpy as np
import cv2


events = [i for i in dir(cv2) if "EVENT" in i] # list all events in cv2 module that contain "EVENT" in their name
#print(events)

def click_event1(event, x, y, flags, param):
    # check if left mouse button is clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"x: {x} y: {y}")
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"{x}, {y}"
        cv2.putText(img, text, (x, y), font, 1, (0, 0, 255), 2)
        cv2.imshow("image", img)

    
    # check if right mouse button is clicked
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0] # get blue channel value 
        green = img[y, x, 1] # get green channel value
        red = img[y, x, 2] # get red channel value
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"{blue}, {green}, {red}"
        cv2.putText(img, text, (x, y), font, 1, (0, 255, 255), 2)
        cv2.imshow("image", img)
        

# draw a line on image between two points clicked by mouse
def click_event2(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow("image", img)        
        
# draw a circle on image where mouse is clicked and show the color of the pixel clicked in a new window
def click_event3(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0] # get blue channel value 
        green = img[y, x, 1] # get green channel value
        red = img[y, x, 2] # get red channel value
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        mycolorImage = np.zeros((512, 512, 3), np.uint8)
        
        # fill the image with the color of the pixel clicked
        mycolorImage[:] = [blue, green, red]
        cv2.imshow("color", mycolorImage)
        
        
        
#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread("assets/img/lena.jpg")
cv2.imshow("image", img)

points = []

# set mouse callback function
cv2.setMouseCallback("image", click_event3)
# (window_name, callback_function)


key = cv2.waitKey(0)
if key == 27 or key == ord("q"):
    cv2.destroyAllWindows()