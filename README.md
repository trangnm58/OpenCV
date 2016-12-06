* Requirements:
- Python 2.7 with numpy and matplotlib
- OpenCV 3.1

* Usage:
- draw_canvas.py:
	```
	python draw_canvas.py
	```
- merge_images.py (put OpenCV logo 'thing.png' on top of my picture 'some.png')
	```
	python merge_images.py
	```
* OpenCV summary
1. GUI features
- Read, show, write image, video
- Draw line, circle, rectangle, ellipse, polygon
- Add text to image, video
- Mouse events
- Trackbar
====> Example: draw_canvas.py

2. Core operations
- ROI (Region of Image)
- Image properties (shape, size)
- Split and Merge image channels (BGR image => B, G, R)
- Make borders for image
- Add images
- Image blending: g(x) = (1-a)*f0(x) + a*f1(x)
- Bitwise operations: and, or, not, xor
====> Example: merge_images.py

3. Image processing
- Change colorspaces (BGR => grayscale or BGR => HSV)
- Image Thresholding
- Geometric Transformations (move, scale, rotate)
	+ Affine Transformation (2D): 2x3 matrix
	+ Perspective Transformation (3D): 3x3 matrix
- Smooth image (blur, denoise):
	+ 2D convolution, filter, kernel
	+ LPF removes noise, HPF detects edges
	+ Averaging, Gaussian, Median, Bilateral (preserve edges)
- Morphological Transformations:
	+ Erosion removes noise but shrinks things, Dilation makes them big again
	+ Opening = erosion + dilation
	+ Closing = dilation + erosion
	+ Morphological Gradient = dilation - erosion
	+ Top Hat = origin - opening
	+ Black Hat = closing - origin
- Image Gradients
- Canny Edge Dectection
- Hough Line, Circle Transform
====> Example: video/video.py
- Image Pyramids: different resolutions of a image stack together
- Contours: boundaries of a shape with same intensity
- Histograms: intensity distribution of an image
	+ Histogram equalization: improve the contrast
- Fourier Transform
- Template Matching

4. Feature Detection

5. Video Analysis
- Object tracking
- Optical Flow
- Background Subtraction
====> Example: video/object_tracking.py

6. Camera Calibration and 3D Reconstruction

7. Machine Learning
- kNN
- SVM
- k-Means

8. Computational Photography
- Image Denoising: average similar patches in different places
- Image Inpainting