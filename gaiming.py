import numpy as np
import os
import cv2

# 遍历文件夹
file = 'D://lixinyu/run_test/'
i = 1
for root, dirs, files in os.walk(file):

    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list

    # 遍历文件
    for f in files:
        if f[-4:]=='.jpg':
            print(f)
            pic = f
            lenna = cv2.imread(file+pic)
            lenna = cv2.resize(lenna, (224,224))

            # cv2.imshow("lenna_gray", lenna_gray.astype("uint8"))
            cv2.imwrite('D://lixinyu/run_test/gaiming/inp_'+str(i)+'.jpg',lenna)
            i = i + 1
