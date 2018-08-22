#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/20 11:35 AM
# @Author: jasmine sun
# @File  : 0016.py

# 纯文本文件 student.txt为学生信息, 写到 student.xls 文件中
from collections import OrderedDict

import json

import xlwt as xlwt


def excel():
    # 读取文件内容
    with open('numbers.txt', 'r') as f:
        content = f.read()
    # 转化为json，注意转化后的dict的元素位置可能和转化前可能不一样，因此需要自定义解码器ordereddict
    # loads()方法把str对象反序列化为json对象
    d = json.loads(content, object_pairs_hook=OrderedDict)
    print(d)
    # 初始化xls文件
    file = xlwt.Workbook()
    # 添加sheet,工作表，名字为test
    table = file.add_sheet('numbers')

    # 读取所有字典，row为序号，i为字典关键字key
    for row, i in enumerate(d):
        # col为序号，j为value,有多个，需要迭代
        print(i)
        for col, j in enumerate(i):
            table.write(row, col, j)
    file.save('numbers.xls')


if __name__ == '__main__':
    excel()
