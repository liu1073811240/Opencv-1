import cv2
import numpy as np
from PIL import Image, ImageFilter

cap = cv2.VideoCapture("1.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
while True:
    ret, frame = cap.read()

    img_arr = frame[..., ::-1]
    img1 = Image.fromarray(img_arr)

    # img2 = img1.filter(ImageFilter.CONTOUR)  # 图像轮廓
    # img2 = img1.filter(ImageFilter.EMBOSS)
    img2 = cv2.cvtColor(img_arr, cv2.COLOR_RGB2GRAY)

    img3_arr = np.array(img2)[..., ::-1]  # 转数据类型和通道
    cv2.imshow("", img3_arr)

    if cv2.waitKey(int(1000/fps)) & 0xFF == ord("q"):
        break
    elif ret == False:
        break

cap.release()  # 关闭视频
cv2.destroyAllWindows()  # 关闭窗口












