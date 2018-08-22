### 任一个英文的纯文本文件，统计其中的单词出现的个数

* list.append(object): 向列表中添加一个对象object
* list.extend(sequence): 把一个序列seq的内容添加到列表中

```import re

# {}: 字典
d = {}


def get_word_frequencies(file_name):
    # splitlines()按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表
    txt = open(file_name, 'r').read().splitlines()
    # print(txt)

    for line in txt:
        line = re.sub(r'[.?!,""/]', ' ', line)  # 要替换的标点符号，英文字符可能出现的
        # print(line)
        # split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
        test1(line.split())
    print(d)


def test1(s):
    # s是一个列表, c是提取出的每一个单词
    for c in s:
        d[c] = (d[c] + 1) if (c in d) else (1)
        # d[c] 统计出每个单词出现的数量
        # print(d[c])


if __name__ == '__main__':
    get_word_frequencies("test.txt")
```

#### 演示
`{'How': 1, 'Successful': 1, 'People': 1, 'Think': 1, 'Good': 1, 'thinkers': 1, 'solve': 1, 'problems': 1, 'they': 2, 'never': 1, 'lack': 1, 'ideas': 1, 'that': 2, 'can': 1, 'build': 1, 'an': 2, 'organization': 1, 'and': 2, 'always': 1, 'have': 1, 'hope': 1, 'for': 1, 'a': 1, 'better': 1, 'future': 1, 'When': 1, 'something': 1, 'intrigues': 1, 'you': 2, 'whether': 1, 'it’s': 1, 'someone': 1, 'else’s': 1, 'idea': 2, 'or': 1, 'the': 1, 'seed': 1, 'of': 2, 'you’ve': 1, 'come': 1, 'up': 1, 'with': 1, 'yourself': 1, 'keep': 2, 'it': 3, 'in': 3, 'front': 1, 'Put': 1, 'writing': 1, 'somewhere': 1, 'your': 2, 'favorite': 1, 'thinking': 2, 'place': 1, 'to': 1, 'stimulate': 1}`
