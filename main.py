import cv2 as cv
import imutils
from pathlib import Path


def write_text(image, counter):
    font = cv.FONT_HERSHEY_COMPLEX
    cv.putText(image, f'Na obrazku wykryto {counter} osoby', (60, 20), font, 0.5, (122, 20, 180), 2)

    return image

# Initializing the HOG person detector
hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

images = Path('images').rglob('*.png')
for path in images:

    # Reading the Image
    image = cv.imread(str(path))

    # Resizing the Image
    image = imutils.resize(image,width=min(400, image.shape[1]))

    # Detecting all the regions in the image that has a pedestrians inside it
    (regions, _) = hog.detectMultiScale(image,winStride=(4, 4),padding=(4, 4),scale=1.05)

    # Drawing the regions in the Image
    counter = 0
    for (x, y, w, h) in regions:
        cv.rectangle(image, (x, y),(x + w, y + h),(0, 0, 255), 2)
        counter += 1

    image = write_text(image, counter)
    #print(f'Na obrazku wykryto {counter} osób')

    # Showing the output Image
    cv.imshow('Image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()