### 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词

```
def get_key(dict):
    print([k for k, v in dict.items() if v == max(d.values())])
```

#### 演示
![](show.png)