#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/16 2:03 PM
# @Author: jasmine sun
# @File  : DNR.py

# PIL验证码图片预处理: https://www.jianshu.com/p/41127bf90ca9
from PIL import Image


# 灰度化
def dnr_img():
    # convert(): 将当前图像转换为其他模式，并且返回新的图像
    img = Image.open('origin.jpg').convert('L')
    img.save('1.jpg', 'jpeg')
    # img.show()
    return img


# 二值化
def binarizing(img, threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    img.save('2.jpg', 'jpeg')
    # img.show()
    return img

# 降噪
# img参数要传一个str类型：Image.open('...')
def depoint(img):
    # load(): 为图像分配内存并从文件中加载它（或者从源图像，对于懒操作）。正常情况下，用户不需要调用这个方法，因为在第一次访问图像时，Image类会自动地加载打开的图像
    pixdata = img.load()
    w, h = img.size
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            count = 0
            if pixdata[x, y - 1] > 10:
                count = count + 1
            if pixdata[x, y + 1] > 10:
                count = count + 1
            if pixdata[x - 1, y] > 10:
                count = count + 1
            if pixdata[x + 1, y] > 10:
                count = count + 1
            if count > 2:
                pixdata[x, y] = 255
    img.save('123.jpg', 'jpeg')
    # img.show()
    return img


if __name__ == '__main__':
    dnr_img()
    binarizing(Image.open('1.jpg'), 100)
    depoint(Image.open('2.jpg'))
