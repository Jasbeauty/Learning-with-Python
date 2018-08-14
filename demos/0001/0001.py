#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/13 4:12 PM
# @Author: jasmine sun
# @File  : 0001.py

# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random, string


def random_str(num, length=7):
    # wb：只写二进制文件，如果文件不存在，自动创建
    f = open('result.txt', 'wb')
    for i in range(num):
        # ascii_letters是生成所有字母，从a - z和A - Z; digits是生成所有数字0 - 9
        chars = string.ascii_letters + string.digits
        # choice()方法返回一个列表，元组或字符串的随机项
        s = [random.choice(chars) for i in range(length)]
        # 如果文件打开模式带b，那写入文件内容时，str(参数)要用encode方法转为bytes形式，否则报错：TypeError: a bytes - like object is required, not 'str'
        # 因为encode返回的是bytes型的数据，不可以和str相加，将‘\n’前加b，write函数参数需要为str类型，转化为str即可
        # str - -->(encode) - -->bytes，bytes - -->(decode) - -->str
        f.write(''.join(s).encode() + b'\n')
    f.close()


if __name__ == '__main__':
    random_str(200)
