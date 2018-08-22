#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/16 4:16 PM
# @Author: jasmine sun
# @File  : 0012.py

# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights
import re


def filter_words():
    words = []
    f = open('filtered_words.txt', 'r')
    for line in f.readlines():
        line = re.sub('[\n]', '', line)
        words.append(line)
    print(words)

    input_word = input("输入词语：")

    Flag = True
    for i in words:
        if i in input_word:
            print("Freedom")
            input_word = input_word.replace(i, '***')
            Flag = False
            # break
    if Flag:
        print("Human Rights")

    print(input_word)


if __name__ == '__main__':
    filter_words()
