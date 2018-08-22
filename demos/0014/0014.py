#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/20 11:35 AM
# @Author: jasmine sun
# @File  : 0014.py

# 纯文本文件 student.txt为学生信息, 写到 student.xls 文件中
# import re
#
# from openpyxl import Workbook
#
#
# def excel():
#     wb = Workbook()
#     ws = wb.create_sheet("student")
#     # ws = wb.create_sheet(title='student')
#
#     data = []
#
#     # re.compile(): 编译正则表达式模式，返回一个对象的模式
#     p = re.compile(':\[')
#     source_file = open('student.txt', 'r')
#     for line in source_file:
#         if not line.startswith('{') and not line.startswith('}'):
#             # strip()方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
#             # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
#             line = line.strip('\n],')
#
#             # sub方法提供一个替换值，可以是字符串或函数，和一个要被处理的字符串
#             line = p.sub(',', line)
#             data.append(line.split(','))
#
#     print(data)
#
#     source_file.close()
#
#     col = 'ABCDE'
#     for i in range(len(data)):
#         for j in range(5):
#             ws[col[j] + str(i + 1)] = data[i][j].strip('"')
#
#     wb.save('student.xlsx')
#
#
# if __name__ == '__main__':
#     excel()

from collections import OrderedDict

import json

import xlwt as xlwt


def excel():
    # 读取文件内容
    with open('student.txt', 'r') as f:
        content = f.read()
    # 转化为json，注意转化后的dict的元素位置可能和转化前可能不一样，因此需要自定义解码器ordereddict：实现对字典对象中元素的排序
    # loads()方法把str对象反序列化为json对象
    d = json.loads(content, object_pairs_hook=OrderedDict)
    print(d)
    # 初始化xls文件
    file = xlwt.Workbook()
    # 添加sheet,工作表，名字为test
    table = file.add_sheet('student')

    # 读取所有字典，row为序号，i为字典关键字key
    for row, i in enumerate(d):
        # 写入（行号，列号，key)
        table.write(row, 0, i)
        # col为序号，j为value,有多个，需要迭代
        for col, j in enumerate(d[i]):
            table.write(row, col + 1, j)
    file.save('student.xls')


if __name__ == '__main__':
    excel()
