import sys
import importlib
import cv2
import numpy as np

import effects


if __name__ == "__main__":
	params = sys.argv[1]  # string
	effect_list = params.split(",")

	cap = cv2.VideoCapture(0)
	while cap.isOpened():
		ret, frame = cap.read()
		frame = cv2.flip(frame, 1)
		# go through effects pipeline
		new_frame = frame
		for e in effect_list:
			func = getattr(effects, e)
			new_frame = func(new_frame)

		cv2.imshow('webcam', frame)
		cv2.imshow('filtered webcam', new_frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
