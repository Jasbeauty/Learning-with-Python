# -*- coding:utf-8 -*-


# 默认参数
def add_end(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L
print(add_end())


# 计算x的n次方
def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
# x=input('输入底数:',x)
# n=input('输入指数:',n)
print(power(2,3))





# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程
import math
def quadratic(a,b,c):
	x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
	x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
	# print(x1,x2)
	return x1,x2
# 测试:

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')





# 对参数类型进行检查,只允许整数和浮点数类型的参数
# 数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if is_int(x):
        return abs(int(x))
    elif is_float(x):
        return abs(float(x))
    else:
        raise TypeError('bad operand type')

def abs(x):
    if x >=0:
        return x
    else:
        return -x

def is_int(x):
    try:
        int(x)
        return True
    except:
        return False

def is_float(x):
    try:
        float(x)
        return True
    except:
        return False

x = input("计算绝对值: ")
print(my_abs(x))



