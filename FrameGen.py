# Program To Read video 
# and Extract Frames 
import cv2 
import time

# Function to extract frames 
def FrameCapture(path): 
	
	# Path to video file 
	vidObj = cv2.VideoCapture(path) 

	# Used as counter variable 
	count = 0

	# checks whether frames were extracted 
	success = 1

	while success: 

		# vidObj object calls read 
		# function extract frames 
		success, image = vidObj.read() 

		# Saves the frames with frame-count 
		if(count %30 == 0):
			cv2.imwrite("wait%d.jpg" % count, image) 
		
		count += 1

# Driver Code 
if __name__ == '__main__': 

	# Calling the function 
	FrameCapture("car1.mp4") 

