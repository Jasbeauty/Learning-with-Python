### 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用

#### 背景知识

##### Tornado

* 一个使用Python编写的一个强大的、可扩展的Web服务器
* 一个轻量级的Web框架，有较为出色的抗负载能力
* 性能优越，不依靠多进程/多线程而达到高性能，最出名的是异步非阻塞的设计方式
* 拥有处理安全性、用户验证、社交网络以及与外部服务（如数据库和网站API）进行异步交互的工具
* 让你能够快速简单地编写高速的Web应用（想编写一个可扩展的社交应用、实时分析引擎，或RESTful API等）

> * [Tornado 官方手册](http://shouce.jb51.net/tornado/ch1.html)
> * [CSDN](https://blog.csdn.net/fengge02/article/details/80045353)
> * [tornado项目的大体结构](https://blog.csdn.net/cdnight/article/details/49618643)
> * [Python Web框架Tornado入门练习小项目：留言板](https://www.oschina.net/code/snippet_2493870_51669)

##### Flask
* Flask 依赖两个外部库：Werkzeug 和 Jinja2

Werkzeug 是一个 WSGI（在 Web 应用和多种服务器之间的标准 Python 接口) 工具集；Jinja2 负责渲染模板
> * [Flask 官方手册](http://docs.jinkan.org/docs/flask/quickstart.html)

##### Jinja2
> * [Jinja2 官方手册](http://docs.jinkan.org/docs/jinja2/templates.html)

```
from datetime import datetime

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
user_list = []


@app.route('/', methods=['GET', 'POST'])
def show_homepage():
    if request.method == 'GET':
        return render_template('comment.html')
    else:
        user_name = request.values.get('user_name')
        # print(user_name)
        user_content = request.values.get('user_content')
        # print(user_content)
        publish_date = datetime.now()
        user_list.append({
            'username': user_name,
            'content': user_content,
            'publish_date': publish_date,
        })

        return render_template('comment.html', users=user_list)


@app.route('/delete', methods=['POST'])
def delete():
    # 数组下标从0开始，所以要减1
    index = int(request.values.get('index')) - 1
    # print(index)
    # pop(): list删除元素
    print(user_list.pop(index))
    print(len(user_list))
    return render_template('comment.html', users=user_list)


if __name__ == '__main__':
    app.run(debug=True)
```


```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>留言簿</title>
</head>

</script>
<body>
    <h1>留言簿</h1>
    <p>请尽情留言吧:</p>
    <form action="/" method="post">
        姓名: <input type="text" placeholder="请输入姓名" value="{{user_name}}" name="user_name" autofocus="autofocus"> <br><br>
        内容: <input placeholder="请输入发表内容" value="{{user_content}}" name="user_content"  width="10px" height="50px" type="text"> <br><br><br>
        <input type="submit" value="提交" name="OK"/>
    </form>
    <h3>留言历史信息</h3>

{#    <form action="/delete" method="post">#}
    {% for user in users %}

         {{ loop.index }}
            <div>
          <p>
             {{ user.username }} -- 留言于({{ user.publish_date }})
          </p>
          <p>
              {{ user.content }}
          </p>
                <form action="/delete" method="post">
                    <input type="hidden" value="{{ loop.index }}"  name="index">
                    <input type="submit" value="删除">
                </form>

        </div>

    {% endfor %}

{#    </form>#}


</body>
</html>
```

#### 演示
myprojects 项目中启动00230024.py，访问 http://127.0.0.1:5000/