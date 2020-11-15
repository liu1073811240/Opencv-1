import cv2

img = cv2.imread("1.jpg", 0)  # 默认1为真彩色，0为灰色

# opencv的图像模式是BGR
cv2.line(img, (10, 10), (100, 100), [0, 0, 255], 3)
cv2.imshow("", img)
cv2.waitKey(10000)
cv2.destroyAllWindows()

