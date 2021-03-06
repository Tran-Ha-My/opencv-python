import cv2
import numpy as np

#VARIABLES

#true while mouse down
drawing = False
ix, iy = -1,-1   # coordinate of point 1 


#FUNCTIONS
def draw_rectangle(event,x,y, flags, params):
    
    global drawing, iy, ix
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)

#SHOWING THE IMAGE



#BLACK

img = np.zeros((512, 512,3))    #note that this 'img' is diff from the 'img' PARAM in the def() above


cv2.namedWindow(winname="my_drawing")
cv2.setMouseCallback('my_drawing', draw_rectangle)

while True:
    cv2.imshow('my_drawing', img)
    if cv2.waitKey(0) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()