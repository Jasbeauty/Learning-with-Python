# -*- coding:utf-8 -*-

import urllib2

url = "http://www.baidu.com"

print('way 1')
response1 = urllib2.urlopen(url)
# 状态码
print(response1.getcode())
# 内容的长度
print(len(response1.read()))


print('way 2')
request = urllib2.urlopen(url)
request.add_header("user-agent",'Chrome')
response2 = urllib2.urlopen(request)
print(response2.getcode())
print(len(response2.read()))


