# coding: utf-8

import numpy as np
import cv2
import random

"""
    随机挑选CNum张图片，进行按通道计算均值mean和标准差std
    先将像素从0～255归一化至 0-1 再计算
"""


train_txt_path = '../../Data/VOC_CNV/ImageSets/Segmentation/train.txt'
voc_path = '../../Data/VOC_CNV/Images/'

CNum = 200     # 挑选多少图片进行计算

img_h, img_w = 32, 32
imgs = np.zeros([img_w, img_h, 3, 1])
means, stdevs = [], []

with open(train_txt_path, 'r') as f:
    lines = f.readlines()
    random.shuffle(lines)   # shuffle , 随机挑选图片

    for i in range(CNum):
        img_path = voc_path + lines[i].rstrip().split()[0] + '.png'

        img = cv2.imread(img_path)
        img = cv2.resize(img, (img_h, img_w))

        img = img[:, :, :, np.newaxis]
        imgs = np.concatenate((imgs, img), axis=3)
        print(i)

imgs = imgs.astype(np.float32)/255.


for i in range(3):
    pixels = imgs[:,:,i,:].ravel()  # 拉成一行
    means.append(np.mean(pixels))
    stdevs.append(np.std(pixels))

means.reverse() # BGR --> RGB
stdevs.reverse()

re_means = [i*255 for i in means]

print("Mean = {}".format(re_means))
print("normMean = {}".format(means))
print("normStd = {}".format(stdevs))
print('transforms.Normalize(normMean = {}, normStd = {})'.format(means, stdevs))
