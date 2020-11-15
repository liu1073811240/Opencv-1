import cv2
import numpy as np

img_arr = np.empty([400, 400, 3], np.uint8)  # 生成空矩阵
print(img_arr)

# [0, 0, 255]
img_arr[..., 0] = 0
img_arr[..., 1] = 0
img_arr[..., 2] = 255  # 将第三个通道的像素值填为255

cv2.imshow("", img_arr)
cv2.waitKey(0)
cv2.destroyAllWindows()


