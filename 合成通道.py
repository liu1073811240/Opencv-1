import cv2
from PIL import Image

img = cv2.imread("1.jpg")

b, g, r = cv2.split(img)

cv2.imshow("b", b)  # 显示灰度图
cv2.imshow("g", g)
cv2.imshow("r", r)

img = cv2.merge([g, r, b])  # 合成通道
cv2.imshow("", img)
cv2.waitKey(0)
cv2.destroyAllWindows()











