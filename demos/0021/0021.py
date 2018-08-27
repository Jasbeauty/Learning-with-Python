#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/22 2:18 PM
# @Author: jasmine sun
# @File  : 0021.py

# 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密

# 使用 salt 加 hash 来单向转换密码明文
import os, hashlib
from _sha256 import sha256
from hmac import HMAC


# 先随机生成 64 bits 的 salt，再选择 SHA-256 算法使用 HMAC 对密码和 salt 进行 10 次叠代混淆，最后将 salt 和 hash 结果一起返回
def encrypt(password, salt=None):
    password = password.encode('utf-8')
    print(password)
    result = password
    if salt is None:
        salt = os.urandom(8)  # 64 bits
    # print(salt)
    # python assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。可以理解assert断言语句为raise - if - not，用来测试表示式，其返回值为假，就会触发异常
    # assert 8 == len(salt)

    # isinstance(s, unicode): 判断s是否是unicode编码，如果是就返回true, 否则返回false
    # assert isinstance(salt, str)

    # if isinstance(password, unicode):
    # password = password.encode('utf-8')
    # print(password)
    # # assert isinstance(password, str)
    #
    # result = password

    for i in range(10):
        result = HMAC(result, salt, sha256).digest()
    print(result)
    return salt + result


def validate_password(hashed, input_password):
    print(encrypt(input_password, salt=hashed[:8]))
    # :8表示前8位
    return hashed == encrypt(input_password, salt=hashed[:8])


if __name__ == '__main__':
    input_password = input("输入密码：")
    hashed = encrypt(input_password)
    print(hashed)
    reput_password = input("再输入一次密码：")
    if validate_password(hashed, reput_password):
        print("right input")
    else:
        print("wrong input")
