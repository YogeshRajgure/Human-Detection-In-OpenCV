import cv2
import imutils
from human_detection import Detector

img = cv2.imread('path_of_image')
img = imutils.resize(img, width=700)
img = Detector(img)
cv2.waitKey(0)
cv2.destroyAllWindows()