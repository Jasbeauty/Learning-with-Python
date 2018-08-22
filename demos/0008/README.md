### 一个HTML文件，找出里面的正文
使用 [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#)
```
from bs4 import BeautifulSoup


def find_body(path):
    f = open(path, 'r')
    soup = BeautifulSoup(f)
    print(soup.body)


if __name__ == '__main__':
    find_body('cartoon/cartoon.html')
```