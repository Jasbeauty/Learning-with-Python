#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/22 3:20 PM
# @Author: jasmine sun
# @File  : test.py


import uuid
import hashlib


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


if __name__ == '__main__':
    new_password = input('Please enter a password: ')
    hashed_password = hash_password(new_password)
    print('The string to store in the db is: ' + hashed_password)
    old_password = input('Now please enter the password again to check: ')
    if check_password(hashed_password, old_password):
        print('You entered the right password')
    else:
        print('I am sorry but the password does not match')