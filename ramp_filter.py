import numpy as np
import cv2

img = cv2.imread('chazhi_5.jpg')
# cv2.resize(img,(224,224))
# j = 80
# while j < 120:
#     for i in range(1, 223):
#             img[i][j] = (img[i][j-1] + img[i][j-2])/2
#     j = j + 1
k = 1
while k < 11:
    for j in range(1,20):
        for i in range(1,224):
            if img[i][k*j][0] > 100:
                img[i][k*j][0] = 255
                img[i][k*j][1] = 255
                img[i][k*j][2] = 255
    k = k + 1
cv2.imshow('1',img)
cv2.waitKey(0)

