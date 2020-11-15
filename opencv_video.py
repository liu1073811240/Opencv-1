import cv2

path = "1.mp4"  # 本地视频路径
# path = r"http://vfx.mtime.cn/Video/2019/03/19/mp4/190319125415785691.mp4"  # 在线视频路径

# cap = cv2.VideoCapture(0)  # 调取内置摄像头
cap = cv2.VideoCapture(path)  # 获取视频对象

fps = cap.get(cv2.CAP_PROP_FPS)  # 从视频对象中获取帧数
print(fps)

w = int(cap.get(3))  # 获取图片的宽度
h = int(cap.get(4))  # 获取图片的高度
# print(w)
# print(h)


fourc = cv2.VideoWriter_fourcc(*"DVIX")  # 视频格式
out = cv2.VideoWriter("2.mp4", fourc, fps, (w, h))  # 写入视频格式

font = cv2.FONT_HERSHEY_COMPLEX
# frame表示读出的每一张图片, ret表示这一张图片是否存在
while True:
    ret, frame = cap.read()
    # 将十六进制数据转成 二进制数据
    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord("q"):  # 视频在播放的过程中按键，循环会中断）。
        break
    elif ret == False:  # 视频播放完了，循环自动中断。
        break
    cv2.rectangle(frame, (200, 50), (300, 150), [0, 0, 255], 3)
    out.write(frame)

    # 前面的1表示字体大小，后面的1表示字体厚度, lineType抗锯齿
    cv2.putText(frame, "beautiful girl 啊", (100, 100), font, 1, (0, 0, 255), 1, lineType=cv2.LINE_AA)
    cv2.imshow("", frame)

cap.release()  # 将视频关了
cv2.destroyAllWindows()
