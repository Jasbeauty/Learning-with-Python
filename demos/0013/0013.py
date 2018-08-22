#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/17 9:59 AM
# @Author: jasmine sun
# @File  : 0013.py


# 用 Python 写一个爬图片的程序 https://unsplash.com/

import io
import json
import os.path
import urllib

import requests
from PIL import Image
from requests.exceptions import RequestException


def get_index(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# 下载并保存到指定目录
def download_pic(url, sequence):
    path = '/Users/wenjiasun/python/Python/demos/0013'
    img = requests.get(url).content
    print(len(img))
    img_size = len(img)
    # filename = '{}/{}'.format(path, 'suibian.jpeg')
    # file = open(filename, 'wb')
    # file.write(img)

    # img_size = os.path.getsize(filename)
    # print(img_size)

    # 判断图片是否大于10M
    if img_size > 10000000:
        folder_name = 'pics10M+'
        # filename = '{}/{}'.format(filename + '/pics10M+', str(sequence) + '.jpeg')
    else:
        folder_name = 'pics'
        # filename = '{}/{}'.format(filename + '/pics', str(sequence) + '.jpeg')

    # 判断文件路径是否存在
    if not os.path.isdir(path):
        os.mkdir(os.path.join(path, folder_name))

    filename = '{}/{}/{}.jpeg'.format(path, folder_name, str(sequence))

    # 读写文件
    file = open(filename, 'wb')
    file.write(img)
    file.close()
    return filename


def main(page, sequence):
    url = 'https://unsplash.com/napi/photos' + '?page=' + str(page)
    html = get_index(url)
    # 字符串转换为json格式
    html = json.loads(html)
    # print(len(html))
    for item in html:
        url = item.get('urls').get('raw')
        print(url)

        # 获取远程图片的size
        # file = urllib.request.urlopen(url)
        # tmpImg = io.BytesIO(file.read())
        # img = Image.open(tmpImg)
        # print(img.size)

        download_pic(url, sequence)
        sequence += 1
    # page += 1
    # main(page, sequence)
    print("download  success!")


if __name__ == '__main__':
    main(1, 1)
