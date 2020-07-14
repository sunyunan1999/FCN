import numpy as np
import os
import cv2

# 遍历文件夹
for i in range(1,421):

    lenna = cv2.imread('G://resnet_dataset/pic_fcn/result_'+str(i)+'.jpg')

    # cv2.imshow("lenna_gray", lenna_gray.astype("uint8"))
    cv2.imwrite('G://resnet_dataset/pic_final/inp_'+str(i)+'.jpg',lenna)
