import cv2
import numpy as np


# Load two images
img1 = cv2.imread('some.png')
img2 = cv2.imread('thing.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)

big = np.hstack((roi,
				cv2.cvtColor(img2gray,cv2.COLOR_GRAY2BGR),
				cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR),
				cv2.cvtColor(mask_inv,cv2.COLOR_GRAY2BGR),
				img1_bg,img2_fg,dst)) #stacking images side-by-side
cv2.imshow('big', big)

img1[0:rows, 0:cols ] = dst
cv2.imshow('img1', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()