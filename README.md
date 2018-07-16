# Python

#### even a raw string cannot end in an odd number of backslashes

> Even in a raw literal, quotes can be escaped with a backslash, but the backslash remains in the result; for example, `r"\""` is a valid string literal consisting of two characters: a backslash and a double quote; `r"\"` is not a valid string literal (even a raw string cannot end in an odd number of backslashes). Specifically, a raw literal cannot end in a single backslash (since the backslash would escape the following quote character). Note also that a single backslash followed by a newline is interpreted as those two characters as part of the literal, not as a line continuation.

#### 格式化的时候 %前面不加逗号

#### input()返回的数据类型是string类型

#### 条件判断语句、循环语句后面要加冒号
> continue语句会直接继续下一轮循环

#### 和list比较，dict有以下几个特点
使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。

#### 函数的参数
* 默认参数  
默认参数必须指向不变对象   
> str、None这样的不变对象，一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象  

* 可变参数  
定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个`*`号
`**extra`表示把`extra`这个dict的所有key-value用关键字参数传入到函数的`**kw`参数，`kw`将获得一个dict，注意`kw`获得的dict是`extra`的一份拷贝，对`kw`的改动不会影响到函数外的`extra`  
> `extra = {'city': 'Beijing', 'job': 'Engineer'}`  
`person('Jack', 24, **extra)` 
  

###### 小结
* Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数
* 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
* 要注意定义可变参数和关键字参数的语法：
> `*args`是可变参数，args接收的是一个tuple；
`**kw`是关键字参数，kw接收的是一个dict  

* 调用函数时如何传入可变参数和关键字参数的语法：
* 可变参数既可以直接传入：`func(1, 2, 3)`，又可以先组装list或tuple，再通过`*args`传入：`func(*(1, 2, 3))`；
* 关键字参数既可以直接传入：`func(a=1, b=2)`，又可以先组装dict，再通过`**kw`传入：`func(**{'a': 1, 'b': 2})`
* 使用`*args`和`**kw`是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
* 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
* 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符`*`，否则定义的将是位置参数。

 
