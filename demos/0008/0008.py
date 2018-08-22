#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/15 4:40 PM
# @Author: jasmine sun
# @File  : 0008.py

# 一个HTML文件，找出里面的正文
from bs4 import BeautifulSoup


def find_body(path):
    f = open(path, 'r')
    soup = BeautifulSoup(f)
    print(soup.body)


if __name__ == '__main__':
    find_body('cartoon/cartoon.html')
