### 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中

> [python 读写 excel](https://www.cnblogs.com/zhangjun1130/archive/2012/10/18/2728760.html)
```
from _elementtree import Element
from xml.etree.ElementTree import Comment, ElementTree, SubElement

import xlrd


def export():
    # 打开Excel文件读取数据
    wb = xlrd.open_workbook(r'../0014/student.xls')
    # 通过名称获取一个工作表
    table = wb.sheet_by_name(u'student')
    data = dict()

    # 循环行列表数据
    for i in range(table.nrows):

        # 获取每一行的数据
        row = table.row(i)

        value_list = list()

        # 获取每一行第一列的值
        key = row[0].value

        for i1 in row[1:]:
            value = i1.value
            value_list.append(value)
        data[key] = value_list
    print(data)

    root = Element('root')
    comment = Comment('学生信息表"id" : [名字, 数学, 语文, 英文]')
    child = SubElement(root, 'students')
    child.append(comment)
    child.text = str(data)
    tree = ElementTree(root)
    tree.write('student.xml', encoding='utf8')


if __name__ == '__main__':
    export()
```

