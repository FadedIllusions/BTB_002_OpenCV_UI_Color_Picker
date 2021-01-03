# RGB Color Picker/Pallete

# Import Needed Packages
import numpy as np
import cv2


# Create A Named Window
cv2.namedWindow("color_picker")

# Create A White Image Fill
fill_val = np.array([255, 255, 255], np.uint8)


# Create Auxilary Callback Function For Trackbars
def trackbar_callback(idx, value):
	fill_val[idx] = value
	

# Create Trackbars For The Channels Of An Image
cv2.createTrackbar('R', 'color_picker', 255, 255, lambda v: trackbar_callback(2,v))
cv2.createTrackbar('G', 'color_picker', 255, 255, lambda v: trackbar_callback(1,v))
cv2.createTrackbar('B', 'color_picker', 255, 255, lambda v: trackbar_callback(0,v))

while True:
	# Use Image Fill To Create 500 x 500 Px Image
	image = np.full((500, 500, 3), fill_val)
	
	# Display Window (With Trackbars)
	cv2.imshow('color_picker', image)
	
	# Define Key Listener
	# If 'ESC': Escape
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
		

# Cleanup
cv2.destroyAllWindows()
