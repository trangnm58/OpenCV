import cv2
import numpy as np


# global variables
drawing = erasing = False
color = (0,0,0)
line_size = 3
cur_x = cur_y = -1

def draw_line(event, x, y, flags, param):
	global drawing, erasing, color, line_size, cur_x, cur_y

	if event == cv2.EVENT_LBUTTONDOWN:
		cur_x, cur_y = x, y
		drawing = True
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing:
			cv2.line(canvas, (cur_x,cur_y), (x,y), color, line_size)
		elif erasing:
			cv2.line(canvas, (cur_x,cur_y), (x,y), (255,255,255), line_size)
		cur_x, cur_y = x, y
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
	elif event == cv2.EVENT_RBUTTONDOWN:
		erasing = True
	elif event == cv2.EVENT_RBUTTONUP:
		erasing = False

def nothing(x):
    pass

# create a white canvas
canvas = np.ones((1024,1024,3), np.uint8) * 255
cv2.namedWindow('canvas')
cv2.setMouseCallback('canvas', draw_line)

# Create a black color_picker
color_picker = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('color_picker')

# create trackbars for color change
cv2.createTrackbar('R','color_picker', 0, 255, nothing)
cv2.createTrackbar('G','color_picker', 0, 255, nothing)
cv2.createTrackbar('B','color_picker', 0, 255, nothing)
cv2.createTrackbar('Size','color_picker', 1, 200, nothing)

while True:
	cv2.imshow('canvas', canvas)
	cv2.imshow('color_picker',color_picker)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	# get current positions of four trackbars
	r = cv2.getTrackbarPos('R', 'color_picker')
	g = cv2.getTrackbarPos('G', 'color_picker')
	b = cv2.getTrackbarPos('B', 'color_picker')
	s = cv2.getTrackbarPos('Size', 'color_picker')

	color_picker[:] = [b,g,r]
	color = (b,g,r)
	line_size = s

cv2.destroyAllWindows()
