autocroppy
==========

Autocroppy is an improvement on traditional autocrop tools. Designed to remove black borders of scanned documents or old slides it stands out on twisted pictures or pictures which black borders are rounded or irregular.

Get Started
-----------

1. You'll need the 32-bit version of Python 2.7. Python 3 is not yet supported, as is 64-bit.
2. Autocroppy depends on OpenCV 2, you can get the newest version here. To get it working with Python follow this guide: http://opencvpython.blogspot.nl/2012/05/install-opencv-in-windows-for-python.html
3. OpenCV depends on NumPy, which can be installed from http://sourceforge.net/projects/numpy/files/NumPy/

Usage
-----

```
python autocroppy [input_folder] [output_folder]
	- input_folder (optional): where to grab images from, defaults to the current directory
	- output_folder (optional): where to put the processed images, defaults to 'out'
```

autocroppy will look for any .jpg files and process them.

Tweaking
--------

If you're looking for a great autocrop algorithm or you want to tweak autocroppy to your needs, this is what you must know.

autocroppy.py is the main file, it contains the code that selects the files and the user interface stuff. If you want to run autocroppy more carefully you can set `INTERACTIVE_MODE` (at the top of the file) to True. autocroppy will now show the original and processed image and ask you if you want to store the result.

autocropper.py contains the `AutoCropper` class which you can use for your own programs. Here is some example code.

```
import cv2
from autocropper import AutoCropper

img = cv2.imread("image.jpg", cv2.IMREAD_COLOR)

ac = AutoCropper(img)
ac.max_border_size = 200 	# defaults to 300
ac.safety_margin = 10 		# defaults to 4, removes extra pixels from the sides to make sure no black remains
ac.tolerance = 10 			# defaults to 4, a gray value is more likely to be considered black when you increase the tolerance

# go!
result = ac.autocrop()
```


