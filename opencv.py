import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('some.png', cv2.IMREAD_GRAYSCALE)
# show image with cv2
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# show image with matplotlib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()
cv2.imwrite('grey.png', img)

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
while cap.isOpened():
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	out.write(frame)
	cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
out.release()
cv2.destroyAllWindows()
