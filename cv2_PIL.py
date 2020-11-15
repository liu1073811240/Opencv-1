import cv2
from PIL import Image

img = cv2.imread("1.jpg")

cv2.line(img, (10, 10), (100, 100), [0, 0, 255], 3)
cv2.rectangle(img, (10, 10), (100, 100), [0, 0, 255], 3)

# h, w, c
# img = img[:, :, ::-1]  # ::-1表示将RGB倒序输出
# BGR通道的图像转换成RGB的图像
img = img[..., ::-1]
img = Image.fromarray(img)
img.show()


