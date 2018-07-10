# -*- coding:utf-8 -*-
import time
from _md5 import md5

import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as pq
import os.path

keyword = 'smile'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'cookie': 'cfduid=d5c702fe59de6a1186abf76190f44b2cd1531048025; locale=en; _ga=GA1.2.1459882886.1531048026; '
              '_gid=GA1.2.4685408.1531048026; _gat=1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/67.0.3396.99 Safari/537.36 '
}


def get_index(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_index(html):
    doc = pq(html)
    # 获取到所有css中class是'.photos .photo-item a img'的标签数组
    links = doc('.photos .photo-item a img')
    # 对标签数组进行遍历获取到存在属性为data-pin-media的标签的url进行返回
    i = -1
    for link in links:
        # split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
        # 语法：str.split(str="",num=string.count(str))[n]
        #   参数说明：
        #       str：表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素
        #       num：表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量
        #       [n]：表示选取第n个分片
        # 注意：当使用空格作为分隔符时，对于中间为空的项会自动忽略
        url = pq(link).attr('data-pin-media').split('?')[0]
        i += 1
        if i < 4:
            # yield返回执行结果并不中断程序执行，return在返回执行结果的同时中断程序执行
            yield url
        else:
            return url


# 下载保存图片
def download_img(url):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.content
        return None
    except RequestException:
        return None


def save_image(content):
    path_name = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    print(path_name)
    if not os.path.exists(path_name):
        with open(path_name, 'wb') as f:
            f.write(content)
            f.close()


def main(page):
    url = 'https://www.pexels.com/search/' + keyword + '/?page=' + str(page)
    html = get_index(url)
    if html:
        urls = parse_index(html)
        for url1 in urls:
            print('正在下载:%r' % url1)
            content = download_img(url1)
            save_image(content)
            print('下载完成:%r' % url1)
            time.sleep(3)
        # print(urls)


# if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行
if __name__ == '__main__':
    # html = requests.get('https://www.pexels.com/search/smile/?page=5')
    # html.encoding = 'utf-8'
    # print(html.text)

    main(5)
