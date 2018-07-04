# -*- coding:utf-8 -*-

# 列表生成式
# [x*x for x in range(1,10)]

# 两层循环
# [m + n for m in 'ABC' for n in 'XYZ']




# generator
s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

        

# 迭代
for i,value in enumerate(['jasmine','fortunate']):
    print(i,value)

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')

# 递归函数
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact_iter(5,1))


def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)

def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)



#参数
def hello(greeting,*args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')

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

# x = input("计算绝对值: ")
print(my_abs(-7))



