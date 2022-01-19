#import numpy as np
#import tensorflow as tf
import cv2 as cv
import imutils


# Initializing the HOG person detector
hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

# Reading the Image
image = cv.imread('side.png')

# Resizing the Image
image = imutils.resize(image,width=min(400, image.shape[1]))

# Detecting all the regions in the image that has a pedestrians inside it
(regions, _) = hog.detectMultiScale(image,winStride=(4, 4),padding=(4, 4),scale=1.05)

# Drawing the regions in the Image
counter = 0
for (x, y, w, h) in regions:
    cv.rectangle(image, (x, y),(x + w, y + h),(0, 0, 255), 2)
    counter += 1

print(f'Na obrazku wykryto {counter} osób')

# Showing the output Image
cv.imshow('Image', image)
cv.waitKey(0)
cv.destroyAllWindows()