import cv2
import numpy as np


def inverse_binary(frame):
	new_frame = cv2.bitwise_not(frame)
	return new_frame

def grayscale(frame):
	new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	return new_frame

def erosion(frame):
	kernel = np.ones((5,5),np.uint8)
	new_frame = cv2.erode(frame, kernel, iterations = 1)
	return new_frame

def dilation(frame):
	kernel = np.ones((5,5),np.uint8)
	new_frame = cv2.dilate(frame, kernel, iterations = 1)
	return new_frame

def opening(frame):
	kernel = np.ones((5,5),np.uint8)
	new_frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
	return new_frame

def closing(frame):
	kernel = np.ones((5,5),np.uint8)
	new_frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
	return new_frame

def gradient(frame):
	kernel = np.ones((5,5),np.uint8)
	new_frame = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)
	return new_frame

def adaptive_threshold_gaussian(frame):
	new_frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
	return new_frame

def bilateral_filter(frame):
	new_frame = cv2.bilateralFilter(frame,5,75,75)
	return new_frame

def median_blur(frame):
	new_frame = cv2.medianBlur(frame,3)
	return new_frame

def laplacian(frame):
	new_frame = cv2.Laplacian(frame, cv2.CV_64F)
	return new_frame

def fast_Nl_means_denoising(frame):
	new_frame = cv2.fastNlMeansDenoising(frame, None, 10, 7, 21)
	return new_frame

def canny(frame):
	new_frame = cv2.Canny(frame, 0, 150, True)
	return new_frame

def clahe(frame):
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	new_frame = clahe.apply(frame)
	return new_frame

def hough_lines_p(frame):
	minLineLength = 200
	maxLineGap = 10
	lines = cv2.HoughLinesP(frame, 1, np.pi/180, 10, minLineLength, maxLineGap)
	new_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
	for x1,y1,x2,y2 in lines[0]:
		cv2.line(new_frame,(x1,y1),(x2,y2),(0,0,255),4)

	return new_frame

