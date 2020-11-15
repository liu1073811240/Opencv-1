import cv2
from PIL import Image
import numpy as np

# 从PIL转换到opencv
img = Image.open("3.jpeg")
img_arr = np.array(img)  # 从图像数据转成numpy数据类型

img_arr = cv2.cvtColor(img_arr, cv2.COLOR_RGB2BGR)  # 转通道
cv2.imshow("", img_arr)
cv2.waitKey(0)

img_arr = img_arr[..., ::-1]

cv2.imshow("", img_arr)
cv2.waitKey(0)
cv2.destroyAllWindows()







