import cv2
import datetime

cap = cv2.VideoCapture(0)


while cap.isOpened():
    ret, frame = cap.read()
    
    if ret:
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"Width: {str(cap.get(3))} Height: {str(cap.get(4))}"
        pos = (10, 50)
        color = (0, 255, 0)
        
        datet = str(datetime.datetime.now()) # return current date and time in format "YYYY-MM-DD HH:MM:SS.SSSSSS"
        
        frame = cv2.putText(frame, datet, pos, font, 1, color, 2)
        
        # frame = cv2.line(frame, (0, 0), (640, 480), (255, 0, 0), 5)
        # frame = cv2.arrowedLine(frame, (0, 240), (320, 240), (0, 0, 255), 5)
        # frame = cv2.rectangle(frame, (320, 0), (640, 240), (255, 255, 0), cv2.FILLED)
        # frame = cv2.circle(frame, (320, 240), 100, (0, 255, 255), 5)


        cv2.imshow("Video",frame)
        
        if cv2.waitKey(1) == ord("q"):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
