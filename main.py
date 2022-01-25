from datetime import datetime
from pathlib import Path

import cv2 as cv
import imutils


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

images = Path('images').rglob('*.png')
for path in images:

    # Reading the Image
    image = cv.imread(str(path))

    # Resizing the Image
    image = imutils.resize(image, width=min(400, image.shape[1]))

    timepoint = datetime.now()

    # Detecting all the regions in the image that has people inside it
    (regions, _) = hog.detectMultiScale(image,
                                        winStride=(4, 4), padding=(4, 4), scale=1.05)

    time = float("{:.2f}".format((datetime.now() - timepoint).total_seconds()))

    # Drawing rectangles on the image
    counter = 0
    for (x, y, w, h) in regions:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        counter += 1

    # Show output image
    cv.imshow('Image', write_text(image, counter, time))
    cv.waitKey(0)
    cv.destroyAllWindows()
