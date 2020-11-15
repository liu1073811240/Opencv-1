import cv2
from PIL import Image
import numpy as np

# 从opencv转换到PIL
img_arr = cv2.imread("3.jpeg")
img_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2RGB)  # 改变通道
img = Image.fromarray(img_arr)  # 改变图像数据类型
img.show()



