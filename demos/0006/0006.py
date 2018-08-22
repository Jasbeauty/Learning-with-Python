#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/15 3:07 PM
# @Author: jasmine sun
# @File  : 0006.py


# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
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
        test1(line.lower().split())
    # print(d)

    # .items()这个函数，把字典形式的键、值，存在了一个元组内
    # x指元组，x[1]是值，x[0]是键

    # reverse = True 表示为倒序排列
    # [-1]表示取出倒数第一个元素
    #  print(sorted(d.items(), key=lambda x: x[1], reverse=True)[0])

    list = sorted(d.items(), key=lambda x: x[1])
    print(max(d.values()))


def test1(s):
    # s是一个列表, c是提取出的每一个单词
    for c in s:
        d[c] = (d[c] + 1) if (c in d) else (1)
        # d[c] 统计出每个单词出现的数量
        # print(d[c])


def get_key(dict):
    print([k for k, v in dict.items() if v == max(d.values())])


if __name__ == '__main__':
    get_word_frequencies("diary.txt")
    get_key(d)
