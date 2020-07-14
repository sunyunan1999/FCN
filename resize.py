import os
import numpy as np
import cv2
import random
import shutil

# 遍历文件夹
# file = 'D://FMCW_Interference/training/'
# for root, dirs, files in os.walk(file):
#
#     # root 表示当前正在访问的文件夹路径
#     # dirs 表示该文件夹下的子目录名list
#     # files 表示该文件夹下的文件list
#
#     # 遍历文件
#     for f in files:
#         if f[-4:]=='.jpg':
#             pic = f
#             name = f[:-4]
#             lenna = cv2.imread(file+pic)
#             lenna = cv2.resize(lenna, (224,224))
#             cv2.imwrite(file+name+'.jpg',lenna)
#             cv2.waitKey()


def moveFile(fileDir_1, fileDir_2, tarDir_1, tarDir_2):
        pathDir = os.listdir(fileDir_1)    #取图片的原始路径
        filenumber=len(pathDir)
        rate=1    #自定义抽取图片的比例，比方说100张抽10张，那就是0.1
        picknumber=int(filenumber*rate) #按照rate比例从文件夹中取一定数量图片
        sample = random.sample(pathDir, picknumber)  #随机选取picknumber数量的样本图片
        print (sample)
        for name in sample:
            shutil.move(fileDir_1+name, tarDir_1+name)
            shutil.move(fileDir_2+name[:-4]+'.png', tarDir_2+name[:-4]+'.png')
        return

if __name__ == '__main__':
    fileDir_1 = 'D://FMCW_Interference/training/'  # 源图片文件夹路径
    fileDir_2 = 'D://FMCW_Interference/mask_gray/'  # 源图片文件夹路径
    tarDir_1 = 'Data_zoo/MIT_SceneParsing/ADEChallengeData2016/images/training/'  # 移动到新的文件夹路径
    tarDir_2 = 'Data_zoo/MIT_SceneParsing/ADEChallengeData2016/annotations/training/'  # 移动到新的文件夹路径
    moveFile(fileDir_1, fileDir_2, tarDir_1, tarDir_2)