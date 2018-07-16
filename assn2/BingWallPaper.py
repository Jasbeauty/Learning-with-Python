#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/7/13 10:40 AM
# @Author: jasmine sun
# @File  : demo.py
import datetime
import subprocess
import requests
from bs4 import BeautifulSoup
import os.path


def set_desktop_background(filename):
    SCRIPT = """/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to POSIX file "%s"
    end tell
    END"""
    # 如果把shell设置成True，指定的命令会在shell里解释执行
    subprocess.Popen(SCRIPT % filename, shell=True)


# 下载并保存到指定目录
def download_pic(url):
    filename = '/Users/wenjiasun/Python/assn2/BingPics'
    img = requests.get(url).content
    # 判断文件路径是否存在
    if not os.path.isdir(filename):
        os.mkdir(filename)
    filename = '{}/{}'.format(filename, str(datetime.datetime.now().strftime("%Y-%m-%d")) + '.jpeg')
    # 读写文件
    file = open(filename, 'wb')
    file.write(img)
    file.close()
    return filename


if __name__ == '__main__':
    result = requests.get('https://cn.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1')
    result.encoding = 'utf-8'
    # 使用BeautifulSoup解析这段代码, 能够得到一个BeautifulSoup的对象, 并能按照标准缩进格式的结构【.prettify()】输出
    # (result.content)是二进制
    soup = BeautifulSoup(result.text, 'lxml')
    # print(soup.prettify())

    # 浏览结构化数据的方法
    url = soup.find('url')
    newurl = 'https://cn.bing.com/' + (url.get_text())
    print(newurl)
    # 下载图片
    filename = download_pic(newurl)
    # 将图片设置为桌面壁纸
    # filename = '/Users/wenjiasun/Desktop/animal.jpg'
    set_desktop_background(filename)
