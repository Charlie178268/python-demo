#encoding=utf-8
import cv2
import numpy as np
img = cv2.imread("./images/baboon2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #灰色化图像
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #亮度、色度、饱和度
cv2.imshow("HelloCV", img)
cv2.imshow("GRAY", gray)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)