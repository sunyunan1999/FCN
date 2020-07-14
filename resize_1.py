import os
import numpy as np
import cv2
import random
import shutil

# 遍历文件夹
file = 'F:/R2019b/bin/training/'
for root, dirs, files in os.walk(file):

    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list

    # 遍历文件
    for f in files:
        if f[-4:]=='.jpg' or f[-4:]=='.png':
            pic = f
            name = f[:-4]
            lenna = cv2.imread(file+pic)
            lenna = cv2.resize(lenna, (224,224))
            cv2.imwrite(file+name+'.jpg',lenna)
            cv2.waitKey()