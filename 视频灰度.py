import cv2
import numpy as np
from PIL import Image, ImageFilter

cap = cv2.VideoCapture("1.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
while True:
    ret, frame = cap.read()
    # img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # HSV是连续的色彩空间

    cv2.imshow("", img1)

    if cv2.waitKey(int(1000/fps)) & 0xFF == ord("q"):
        break
    elif ret == False:
        break

cap.release()  # 关闭视频
cv2.destroyAllWindows()  # 关闭窗口