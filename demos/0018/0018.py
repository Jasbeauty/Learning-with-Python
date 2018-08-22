#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/21 4:00 PM
# @Author: jasmine sun
# @File  : 0018.py

# 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中

from _elementtree import Element
from xml.etree.ElementTree import Comment, ElementTree, SubElement

import xlrd


def export():
    # 打开Excel文件读取数据
    wb = xlrd.open_workbook(r'../0015/city.xls')
    # 通过名称获取一个工作表
    table = wb.sheet_by_name(u'city')
    data = dict()

    # 循环行列表数据
    for i in range(table.nrows):
        # 获取每一行的数据
        row = table.row(i)
        # print(row)

        key = row[0].value
        # print(key)
        for i1 in row[1:]:
            value = i1.value
        data[key] = value
    print(data)

    root = Element('root')
    comment = Comment('城市信息')
    child = SubElement(root, 'cities')
    child.append(comment)
    child.text = str(data)
    tree = ElementTree(root)
    tree.write('city.xml', encoding='utf8')


if __name__ == '__main__':
    export()
