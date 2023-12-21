import cv2

cap = cv2.VideoCapture(0) # 0 = default camera -- 1 = external camera
#cap = cv2.VideoCapture('video.mp4') # for video file 
 
# save video 
out = cv2.VideoWriter("src/assets/saved_frames/output.avi", cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640,480)) 
# (path, codec, fps, size) -> codec = 4-character code of codec used to compress the frames (eg. XVID, MJPG, DIVX, X264, WMV1, WMV2) -> fps = frames per second -> size = width and height of the frames in the video

# you can also use the following syntax to save video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("assets/saved_frames/output.avi", fourcc, 20.0, (640,480))

#cap.isOpened() # if you are reading from a video file, it will return true if the file exists and can be read
while True:  # you can also use while(cap.isOpened()):
    ret, frame = cap.read() #  ret is a boolean that returns true if the frame is available 
    
    if ret:
        
        # get() method is used to fetch the properties of the video source -> https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
        print(f"prop: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}") # 3
        print(f"prop: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}") # 4

        # set property of camera 
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        # (propId, value)

        print(f"prop: {cap.get(3)}") # cv2.CAP_PROP_FRAME_WIDTH
        print(f"prop: {cap.get(4)}") # cv2.CAP_PROP_FRAME_HEIGHT
        
        
        # write the frame to the file
        out.write(frame)
        
        # convert frame to grayscale
        grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        
        # show the frame
        cv2.imshow('frame', frame)
        
        # wait for key press to close window q = quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
# closes video file or capturing device and destroys all windows
cap.release()
out.release()
cv2.destroyAllWindows()