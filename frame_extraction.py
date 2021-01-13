import cv2 
import os 
  
# Read the video from specified path 
cam = cv2.VideoCapture("C:\\Users\\nipun\\Videos\\y2mate.com - Classroom surveillance 3_480p.mp4") 


try: 
      
    # creating a folder named data 
    if not os.path.exists('D:\\classroom_data'): 
        os.makedirs('D:\\classroom_data') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
  
while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images
        if(currentframe%10 ==0):
            name = 'D:\\classroom_data\\frame' + str(currentframe) + '.jpg'
            
            print ('Creating...' + name) 
      
            # writing the extracted images 
            cv2.imwrite(name, frame) 
      
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
