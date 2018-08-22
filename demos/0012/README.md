### 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」
```
import re


def filter_words():
    words = []
    f = open('filtered_words.txt', 'r')
    for line in f.readlines():
        line = re.sub('[\n]', '', line)
        words.append(line)
    print(words)

    input_word = input("输入词语：")

    Flag = True
    for i in words:
        if i in input_word:
            print("Freedom")
            input_word = input_word.replace(i, '***')
            Flag = False
            # break
    if Flag:
        print("Human Rights")

    print(input_word)


if __name__ == '__main__':
    filter_words()
```

#### 演示
```
输入词语：你好，北京
Freedom
你好，***
```
