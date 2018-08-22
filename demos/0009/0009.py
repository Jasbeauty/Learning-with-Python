#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/15 5:09 PM
# @Author: jasmine sun
# @File  : 0009.py

from bs4 import BeautifulSoup


def find_body(path):
    f = open(path, 'r')
    soup = BeautifulSoup(f)
    print(soup.find_all('a'))


if __name__ == '__main__':
    find_body('cartoon/cartoon.html')
