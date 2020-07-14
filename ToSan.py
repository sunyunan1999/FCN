import numpy as np
import cv2
import os

# 遍历文件夹
file = 'label/'
for root, dirs, files in os.walk(file):

    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list

    # 遍历文件
    for f in files:
        if f[-4:]=='.jpg':
            print(f)
            name = f[:-4]
            pic = f
            lenna = cv2.imread(file+pic)
            row, col, channel = lenna.shape
            lenna_gray = np.zeros((row, col))

            for r in range(row):
                for l in range(col):
                    # print(str(lenna[r,l,0])+'/'+str(lenna[r,l,1])+'/'+str(lenna[r,l,2]))

                    if lenna[r, l, 1] < 150:
                        lenna_gray[r,l] = 255  # 白色 背景 255 2
                        if (lenna[r, l, 2] > 200):
                            # print(str(lenna[r,l,0])+'/'+str(lenna[r,l,1])+'/'+str(lenna[r,l,2]))
                            lenna_gray[r,l] = 150 # 灰色 噪声 150 1
                    else:
                        lenna_gray[r,l] = 1 # 黑色 信号 1 0

            # cv2.imshow("lenna_gray", lenna_gray.astype("uint8"))
            cv2.imwrite('label_san/'+name+'.png',lenna_gray)
            cv2.waitKey()
