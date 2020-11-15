import cv2
from PIL import Image

# 将图像变为单通道
img = cv2.imread("1.jpg")

img[..., 1] = 0
img[..., 2] = 0

cv2.imshow("", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



