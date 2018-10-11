import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
	_, frame = cap.read()

	convert = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	cv2.imshow("orignal", frame)
	cv2.imshow("converted", convert)

	print("\n")
	print("PRESS 'q' to exit")
	
	key = cv2.waitKey(1) & 0xFF
	if(key == ord('q')):
		break

cv2.destroyAllWindows()
