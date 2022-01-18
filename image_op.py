import cv2
import imutils
from human_detection import Detector

img = cv2.imread('abcde.jpg')
img = imutils.resize(img, width=700)
img = Detector(img)
cv2.waitKey(0)
cv2.destroyAllWindows()