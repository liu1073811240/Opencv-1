import cv2
from PIL import Image

img = cv2.imread("1.jpg")
cv2.line(img, (10, 10), (100, 100), [0, 0, 255], 3)
cv2.rectangle(img, (10, 10), (100, 100), [0, 0, 255], 3)

cv2.imshow("", img)
cv2.waitKey(0)
cv2.destroyAllWindows()





