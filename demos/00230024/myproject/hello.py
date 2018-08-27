#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/8/23 2:52 PM
# @Author: jasmine sun
# @File  : hello.py
from flask import Flask, url_for, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/index/')
def index():
    return 'index'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>', methods=['POST'])
def show_post(post_id):
    username = request.values.get('username')
    password = request.values.get('password')
    # show the post with the given id, the id is an integer
    return jsonify({
        'username': username,
        'password': password
    })


@app.route('/login')
def login(): pass


@app.route('/static', endpoint='statisc')
def static(): pass


@app.route('/hello/', methods=['GET', 'POST'])
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# 单元测试的最简单的解决方案是：用 test_request_context() 环境管理器。结合 with 声明，绑定一个测试请求，这样你才能与之交互
with app.test_request_context():
    # url_for()用来给指定的函数构造URL。它接受函数名作为第一个参数，也接受对应URL规则的变量部分的命名参数。未知变量部分会添加到URL末尾作为查询参数
    print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='jasmine', forward='/'))
    print(url_for('static', filename='style.css'))

if __name__ == '__main__':
    app.run(debug=True)
