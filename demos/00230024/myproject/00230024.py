#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/24 11:00 AM
# @Author: jasmine sun
# @File  : demo.py


# 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用


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
