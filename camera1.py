import cv2

cap = cv2.VideoCapture(0)   #default camera = 0

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   #interger- can be 1080, for example
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


writer = cv2.VideoWriter('../DATA/myFirstVid.mp4', cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height)) # SAVE the video to the location where this script is



while True:
    ret, frame = cap.read()   # 'Tuple unpacking' = ret, frame bc cap.read() grab a frame => return msg is a tuple => tuple unpacking
    
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    
    # OPERATIONS (drawings etc)...
    
    writer.write(frame)
    
    cv2.imshow('frame', frame)
    
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
        
        
cap.release()
writer.release()
cv2.destroyAllWindows()
                                #frame = single img => video = returns a series of image (continually updating the image)
                                # General idea: treat it like an image (frame) & continually updating that frame
        
        
# the 2nd param in VideoWriter() is important, you'll have to specify what video codec you want to save it for diff platform : macOS == (*'XVID') ;  Windows == (*'DIVX')
# The 3rd param in VideoWriter is frames per second