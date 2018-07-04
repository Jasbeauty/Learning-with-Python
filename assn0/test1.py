#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# range()函数可以生成一个整数序列，再通过list()函数可以转换为list
list=list(range(5))
print(list)

sum=0
for x in range(101):
	sum=sum+x
print('1-100相加的和：',sum)


sum=0
n=99
while n>0:
	sum=sum+n
	n=n-2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
	print('Hello,',x)


height=1.75
weight=80.5
bmi=80.5//(1.75*1.75)
print('bmi =',bmi)
if bmi<18.5:
	print('过轻')
elif 18.5<=bmi<25:
	print('正常')
elif 25<=bmi<28:
	print('过重')
elif 28<=bmi<32:
	print('肥胖')
elif bmi>=32:
	print('严重肥胖')



#tuple和list非常类似，但是tuple一旦初始化就不能修改(tuple用小括号，list用中括号)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])
# 格式化
print('hi,%s,you have $%d' %('Michael',1000000))

s1=72
s2=85
r=(85-72)/72*100
print('%.1f %%' % r)



# print absolute value of an integer
a = 100
if a>=0:
	print(a)
else:
	print(-a)

# 输入多行内容
print(r'''line1
line2
line3''')

# r'..'引号里的字符串默认不转义[即使是原始（raw）字符串末尾也不能带奇数个反斜杠，因为这会引起后续引号的转义]
print(r'''hello,\n
world''')

# 这种变量本身类型不固定的语言称之为动态语言
a=123
print(a)
b=a
a='ABC'
print(b)

# -*- coding: utf-8 -*-
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n,f,s1,s2,s3,s4)