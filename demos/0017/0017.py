#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/20 2:46 PM
# @Author: jasmine sun
# @File  : 0017.py

# 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中
from _elementtree import Element
from xml.etree.ElementTree import Comment, ElementTree, SubElement

import xlrd


def export():
    # 打开Excel文件读取数据
    wb = xlrd.open_workbook(r'../0014/student.xls')
    # 通过名称获取一个工作表
    table = wb.sheet_by_name(u'student')
    data = dict()

    # 循环行列表数据
    for i in range(table.nrows):
        # 获取整行和整列的值（数组）
        # print(table.row_values(i))
        # 使用行列索引
        # print(table.row(i)[2].value)

        # 获取每一行的数据
        row = table.row(i)
        print(row)
        value_list = list()
        key = row[0].value
        print(key)
        for i1 in row[1:]:
            value = i1.value
            print(value)
            value_list.append(value)
        data[key] = value_list
    print(data)

    root = Element('root')
    comment = Comment('学生信息表"id" : [名字, 数学, 语文, 英文]')
    child = SubElement(root, 'students')
    child.append(comment)
    child.text = str(data)
    tree = ElementTree(root)
    tree.write('student.xml', encoding='utf8')


if __name__ == '__main__':
    export()
