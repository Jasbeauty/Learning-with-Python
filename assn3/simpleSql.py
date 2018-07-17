#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/7/16 3:27 PM
# @Author: jasmine sun
# @File  : simpleSql.py

import pymysql
# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password='sunwenjia', db='test')
# 开启自动提交SQL，如果这里不设置，以后的命令需要执行conn.commit()来提交执行，否则都在内存中
conn.autocommit(False)
# 创建游标
cursor = conn.cursor()
# # 执行普通SQL，并返回受影响行数
# effect_row = cursor.execute("insert into test1 values (4, 'Danny')")
# print(effect_row) # out：1
# # 提交
# conn.commit()
# cursor.execute('select * from test1')
# # 获取第一行数据
# row_1 = cursor.fetchall()
# print(row_1) # out:  (1, 'Boss')
# # 关闭游标
# cursor.close()
# # 关闭连接
# conn.close()



# 查询语句  test1表名
# sql_select = "select * from test1"
# try:
#     cursor.execute(sql_select)  # 执行sql语句
#     results = cursor.fetchall()  # 获取查询的所有记录
#     print("id", "name")
#     # 遍历结果
#     for row in results:
#         id = row[0]
#         name = row[1]
#         print(id, name)
# except Exception as e:
#     raise e
# finally:
#     conn.close()  # 关闭连接





# 插入操作
# sql_insert = "insert into test1(id,name) values(5, 'fortunate')"
# try:
#     cursor.execute(sql_insert)
#     # 提交
#     conn.commit()
# except Exception as e:
#     # 错误回滚
#     conn.rollback()
# finally:
#     conn.close()


# 更新操作
# sql_update = "update test1 set name = '%s' where id = %d"
#
# try:
#     cursor.execute(sql_update % ("dongge", 3))  # 像sql语句传递参数
#     # 提交
#     conn.commit()
# except Exception as e:
#     # 错误回滚
#     conn.rollback()
# finally:
#     conn.close()


sql_delete = "delete from test1 where id = %d"

try:
    cursor.execute(sql_delete % (4))  # 像sql语句传递参数
    # 提交
    conn.commit()
except Exception as e:
    # 错误回滚
    conn.rollback()
finally:
    conn.close()