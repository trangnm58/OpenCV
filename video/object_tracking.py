import sys
import importlib
import cv2
import numpy as np


def nothing(x):
	pass

if __name__ == "__main__":
	# Trackbar for HSV
	HSV_picker = np.zeros((1,380,3), np.uint8)
	cv2.namedWindow('HSV_picker')
	# create trackbars for HSV change
	cv2.createTrackbar('H1','HSV_picker', 0, 255, nothing)
	cv2.createTrackbar('H2','HSV_picker', 0, 255, nothing)
	cv2.createTrackbar('S1','HSV_picker', 0, 255, nothing)
	cv2.createTrackbar('S2','HSV_picker', 0, 255, nothing)
	cv2.createTrackbar('V1','HSV_picker', 0, 255, nothing)
	cv2.createTrackbar('V2','HSV_picker', 0, 255, nothing)

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

	# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
	term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

	while cap.isOpened():
		# HSV picker
		cv2.imshow('HSV_picker',HSV_picker)
		# get current HSV of 3 trackbars
		h1 = cv2.getTrackbarPos('H1', 'HSV_picker')
		s1 = cv2.getTrackbarPos('S1', 'HSV_picker')
		v1 = cv2.getTrackbarPos('V1', 'HSV_picker')
		h2 = cv2.getTrackbarPos('H2', 'HSV_picker')
		s2 = cv2.getTrackbarPos('S2', 'HSV_picker')
		v2 = cv2.getTrackbarPos('V2', 'HSV_picker')

		# calculate the mask
		mask = cv2.inRange(hsv_roi, np.array((h1, s1, v1)), np.array((h2, s2, v2)))
		roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,255])
		cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

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
