#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/22 11:47 AM
# @Author: jasmine sun
# @File  : 0019.py

# 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中
from _elementtree import Element
from xml.etree.ElementTree import Comment, ElementTree, SubElement

import xlrd


def export():
    # 打开Excel文件读取数据
    wb = xlrd.open_workbook(r'../0016/numbers.xls')
    # 通过名称获取一个工作表
    table = wb.sheet_by_name(u'numbers')
    data = list()

    # 循环行列表数据
    for i in range(table.nrows):
        # 获取每一行的数据
        row = table.row_values(i)
        # print(row)
        data.append(row)

    print(data)

    root = Element('root')
    comment = Comment('数字信息')
    child = SubElement(root, 'numbers')
    child.append(comment)
    child.text = str(data)
    tree = ElementTree(root)
    tree.write('numbers.xml', encoding='utf8')


if __name__ == '__main__':
    export()
