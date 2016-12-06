import sys
import importlib
import cv2
import numpy as np


if __name__ == "__main__":
	cap = cv2.VideoCapture(0)
	# take first frame of the video
	ret,frame = cap.read()
	frame = cv2.flip(frame, 1)

	# setup initial location of window
	r,h,c,w = 250,250,400,400  # simply hardcoded the values
	roi_rect = cv2.rectangle(frame,(r,h),(c,w),(0,255,0),3)
	cv2.imshow('region of image', roi_rect)
	track_window = (c,r,w,h)

	# set up the ROI for tracking
	roi = frame[r:r+h, c:c+w]
	hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv_roi, np.array((10., 60., 40.)), np.array((180.,255.,255.)))
	roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,255])
	cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

	# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
	term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

	while cap.isOpened():
		ret, frame = cap.read()
		frame = cv2.flip(frame, 1)
		if ret == True:
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
			cv2.imshow('dst', dst)
			# apply CamShift to get the new location
			ret, track_window = cv2.CamShift(dst, track_window, term_crit)

			# Draw it on image
			x,y,w,h = track_window
			img2 = cv2.circle(frame, (x+w/2,y+h/2), (x+w)/10, (0,0,200), -1)
			cv2.imshow('img2', img2)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		else:
			break

	cap.release()
	cv2.destroyAllWindows()
