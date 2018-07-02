# Python

### even a raw string cannot end in an odd number of backslashes

> Even in a raw literal, quotes can be escaped with a backslash, but the backslash remains in the result; for example, r"\"" is a valid string literal consisting of two characters: a backslash and a double quote; r"\" is not a valid string literal (even a raw string cannot end in an odd number of backslashes). Specifically, a raw literal cannot end in a single backslash (since the backslash would escape the following quote character). Note also that a single backslash followed by a newline is interpreted as those two characters as part of the literal, not as a line continuation.

### 格式化的时候 %前面不加逗号

### input()返回的数据类型是string类型

### 条件判断语句、循环语句后面要加冒号
> continue语句会直接继续下一轮循环

### 和list比较，dict有以下几个特点：
使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
