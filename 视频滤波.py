import cv2
import numpy as np
from PIL import Image, ImageFilter

cap = cv2.VideoCapture("1.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
while True:
    ret, frame = cap.read()
    img_arrs = frame[..., ::-1]
    imgs = Image.fromarray(img_arrs)

    img = imgs.filter(ImageFilter.MinFilter(5))
    img_arr = np.array(img)[..., ::-1]
    cv2.imshow("", img_arr)

    if cv2.waitKey(int(1000/fps)) & 0xFF == ord("q"):
        break
    elif ret == False:
        break

cap.release()  # 关闭视频
cv2.destroyAllWindows()  # 关闭窗口