from datetime import datetime
from pathlib import Path

import cv2 as cv
import imutils

# add text to image
def write_text(image, counter, time):
    font = cv.FONT_HERSHEY_COMPLEX

    # text, coordinate, font, text size, color, thickness of font
    cv.putText(image, f'Na obrazku wykryto {counter} osoby',
               (60, 20), font, 0.5, (122, 20, 180), 2)
    cv.putText(image, f'Detekcja zajela: '
               + str(time)
               ,(60, 180), font, 0.5,
               (122, 20, 180), 2)
    return image


# Initializing the HOG person detector
hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

# creating list of image paths in given directory
images = Path('images').rglob('*.png')
for path in images:

    # reading the image
    image = cv.imread(str(path))

    # resizing the image
    image = imutils.resize(image, width=min(400, image.shape[1]))

    # start counting time
    timepoint = datetime.now()

    # detecting all the people on the picture
    (regions, _) = hog.detectMultiScale(image,
                                        winStride=(4, 4), padding=(4, 4), scale=1.05)

    # stop counting time
    time = float("{:.2f}".format((datetime.now() - timepoint).total_seconds()))

    # drawing rectangles on the image
    counter = 0
    for (x, y, w, h) in regions:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        counter += 1

    # show output image
    cv.imshow('Image', write_text(image, counter, time))
    cv.waitKey(0)
    cv.destroyAllWindows()
