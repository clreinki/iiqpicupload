# face detection with mtcnn on a photograph
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from mtcnn.mtcnn import MTCNN
from PIL import Image
import cv2
import os

# Fixes blue color
def bgr_to_rbg(img):
    """Given a BGR (cv2) numpy array, returns a RBG (standard) array."""
    dimensions = len(img.shape)
    if dimensions == 2:
        return img
    return img[..., ::-1]

# draw an image with detected objects
def draw_image_with_boxes(filename, result_list):
	# load the image
	data = pyplot.imread(filename)
	# plot the image
	pyplot.imshow(data)
	# get the context for drawing boxes
	ax = pyplot.gca()
	# plot each box
	for result in result_list:
		# get coordinates
		x, y, width, height = result['box']
		# create the shape
		rect = Rectangle((x, y), width, height, fill=False, color='red')
		# draw the box
		ax.add_patch(rect)
	# show the plot
	pyplot.show()

filename = '350062.jpg'
# load image from file
#pixels = pyplot.imread(filename)
pixels = cv2.imread(filename)
# create the detector, using default weights
detector = MTCNN()
# detect faces in the image
faces = detector.detect_faces(pixels)
print(faces)

# ====== Actual cropping ======
x1, y1, width, height = faces[-1]['box']
x2, y2 = x1 + width, y1 + height
#image = image[pos[0] : pos[1], pos[2] : pos[3]]
xoff = round((150 - width)/2)
yoff = round((150 - height)/2)
print(xoff)
print(yoff)
y1 = y1 - yoff
y2 = y2 + yoff
x1 = x1 - xoff
x2 = x2 + xoff
image = bgr_to_rbg(pixels[y1:y2, x1:x2])
pyplot.imshow(image)
pyplot.show()
# Resize
#image = cv2.resize(
#    image, (self.width, self.height), interpolation=cv2.INTER_AREA
#)

# display faces on the original image
draw_image_with_boxes(filename, faces)