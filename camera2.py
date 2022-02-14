import cv2
#import time


cap = cv2.VideoCapture('DATA/hand_move.mp4')

if cap.isOpened() == False:
    print('ERROR FILE NOT FOUND OR WRONG CODEC USED !')
    
while cap.isOpened():
    ret, frame = cap.read()
    
    if ret == True:
        
        # WRITER 20 FPS
        #time.sleep(1/20)            # delay 1/framerate seconds (bc it's frames / 1sec duH)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
    else:
        break    # while capture is not working, break out of the While loop (it's lined up with the 1st 'if')
        
cap.release()
cv2.destroyAllWindows()


# The code was fine, until the video is played too fast ! 
# -> import time module (python built-in)  => PLAY at the SAME FRAME RATE as it was RECORDED