import scipy.misc as misc
import numpy as np
from PIL import Image

path = 'D:/Data/deeplearning/FCN/Data_zoo/MIT_SceneParsing/ADEChallengeData2016/images/FMCW_Interference/test/'

a = list(range(1,201))

def GetResult(index):  # 将原图与预测标签图对应相乘，得分割图
    pred = misc.imread(path + 'pred_' + str(index) + '.png')
    pred_np = np.array(pred)
    alpha = 1

    ini = misc.imread(path + 'inp_' + str(index) + '.jpg')
    result_pred = np.zeros([224, 224, 3], dtype=np.uint8)
    # result_label = np.zeros([256,256,3],dtype=np.uint8)

    for i in range(224):
        for j in range(224):
            if pred_np[i][j] == 1:  # 分类为背景
                # result_pred[i][j][0] = int(alpha * ini[i][j][0])
                # result_pred[i][j][1] = int(alpha * ini[i][j][1])
                # result_pred[i][j][2] = int(alpha * ini[i][j][2])
                result_pred[i][j] = [0, 0, 0]
            else:  # 分类为老城区，蓝色
                # result_pred[i][j][0] = int(alpha * ini[i][j][0])
                # result_pred[i][j][1] = int(alpha * ini[i][j][1])
                # result_pred[i][j][2] = int(alpha * ini[i][j][2] + (1 - alpha) * 255)
                result_pred[i][j] = [255, 255, 255]
                # for p in range(-5,5):
                #     for k in range(-5,5):
                #         if (((i+p) > 0) & ((i+p) < 224) & ((j+k) > 0) & ((j+k) < 224)):
                #             result_pred[i+p][j+k] = [255, 255, 255]


    result_pred_img = Image.fromarray(result_pred)
    result_pred_img.save(path + 'result_' + str(index) + '.jpg')

def GetMerge(index):  # 将原图与分割图合并
    UNIT_SIZE = 224  # 单个图像的大小为229*229
    TARGET_WIDTH = 2 * UNIT_SIZE  # 拼接完后的横向长度为6*229

    index = str(index)
    target = Image.new('RGB', (TARGET_WIDTH, UNIT_SIZE))
    initial = Image.open(path + 'inp_' + index + '.jpg')
    result = Image.open(path + 'result_' + index + '.jpg')

    right = UNIT_SIZE

    target.paste(initial, (0, 0, right, UNIT_SIZE))  # 将image复制到target的指定位置中
    target.paste(result, (UNIT_SIZE, 0, 2 * UNIT_SIZE, UNIT_SIZE))
    quality_value = 100  # quality来指定生成图片的质量，范围是0～100
    target.save(path + 'merge_' + index + '.jpg', quality=quality_value)


for i in a:
    GetResult(i)
    GetMerge(i)