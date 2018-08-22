#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/14 11:32 AM
# @Author: jasmine sun
# @File  : 0004.py

# 任一个英文的纯文本文件，统计其中的单词出现的个数


import re

# {}: 字典
d = {}


def get_word_frequencies(file_name):
    # splitlines()按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表
    txt = open(file_name, 'r').read().splitlines()
    # print(txt)

    for line in txt:
        line = re.sub(r'[.?!,""/]', ' ', line)  # 要替换的标点符号，英文字符可能出现的
        # print(line)
        # split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
        test1(line.split())
    print(d)


# def test():
#     s = 'here is a sample of english text a'.split()
#     d = {}
#     for c in s:
#         d[c] = (d[c] + 1) if (c in d) else (1)


def test1(s):
    # s是一个列表, c是提取出的每一个单词
    for c in s:
        d[c] = (d[c] + 1) if (c in d) else (1)
        # d[c] 统计出每个单词出现的数量
        # print(d[c])


if __name__ == '__main__':
    get_word_frequencies("test.txt")
