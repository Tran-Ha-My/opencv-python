import cv2

# GLOBAL VARIABLES

pt1 = (0,0)
pt2 = (0,0)

top_left_clicked = False
bottom_right_clicked = False



# CALLBACK FUNCTION RECTANGLE

def draw_rectangle( event, x,y, flags, param):
    global pt1, pt2, top_left_clicked, bottom_right_clicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        # RESET THE RECTANGLE...
        if top_left_clicked and bottom_right_clicked:
            
            pt1 = (0,0)
            pt2 = (0,0)
            top_left_clicked = False
            bottom_right_clicked = False
    
        # DRAW RECTANGLE
        if top_left_clicked == False:
            
            pt1 = (x,y)
            top_left_clicked = True
            
        elif bottom_right_clicked == False:
            pt2 = (x,y)
            bottom_right_clicked = True
            
    
# GLOBAL VARIABLES
cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', draw_rectangle)


while True:
    
    ret, frame = cap.read()
    
    
    # CONNECT TO THE CALLBACK...
    if top_left_clicked:
        cv2.circle(frame, center = pt1, radius = 5, color = (0,0,255), thickness = -1)

    if top_left_clicked and bottom_right_clicked:
        cv2.rectangle(frame, pt1, pt2, color =(0,0,255), thickness = 2)
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()