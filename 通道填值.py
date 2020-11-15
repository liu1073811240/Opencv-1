import cv2
import numpy as np

img_arr = np.zeros([400, 400, 3], np.uint8)
# img_arr = np.ones([400, 400, 3])

# img_arr = np.arange(400*400*3).reshape([400, 400, 3]) / (400*400*3)
# img_arr = np.random.rand(400, 400, 3)
# img_arr = np.random.randn(400, 400, 3)
# img_arr = np.random.normal(0, 0.5, (400, 400, 3))

cv2.imshow("", img_arr)  # opencv中 像素值填0-1之间的值
cv2.waitKey(0)
cv2.destroyAllWindows()


