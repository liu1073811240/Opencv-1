import cv2

img = cv2.imread("1.jpg")
# print(type(img))
# print(img)

img_size = img.shape
print(img_size)
img = cv2.resize(img, (img_size[1]//2, img_size[0]//2))

cv2.imshow("img", img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
cv2.imwrite("2.jpg", img)





