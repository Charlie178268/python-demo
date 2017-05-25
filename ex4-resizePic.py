#encoding=utf-8
import cv2
img = cv2.imread("./images/bear.jpg")
print img.shape
h = img.shape[0]
w = img.shape[1]
img2 = cv2.resize(img, (2*h, 2*w), interpolation=cv2.INTER_CUBIC)#放大两倍
cv2.imshow("HelloCV", img2)
cv2.imshow("HelloCV1", img)
cv2.waitKey(0)