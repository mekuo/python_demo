#!/usr/bin/env python
# _*_ coding:UTF-8 _*_
import pymysql
conn = pymysql.connect(
    user="root",
    password="",
    port=3306,
    host="127.0.0.1",
    db="pytest",
    charset="utf8"
)
cursor=conn.cursor()          #获取对应的操作游标
print(cursor)
# url='https://images.unsplash.com/photo-1442508748335-fde9c3f58fd9?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=efb6133a444ebb07753d8fa38eb6d2f6&w=1000&q=80'
#
# sql = "INSERT INTO curl_image (`url`) VALUES ( '%s' )" % url
# cursor.execute(sql)
# conn.commit()
# print('成功修改', cursor.rowcount, '条数据')

sql_1 = "UPDATE curl_finance SET saving = saving + 2000 WHERE account = '18012345678' "
sql_2 = "UPDATE curl_finance SET expend = expend + 1000 WHERE account = '18012345678' "
sql_3 = "UPDATE curl_finance SET income = income + 2000 WHERE account = '18012345678' "

try:
    cursor.execute(sql_1)  # 储蓄增加1000
    cursor.execute(sql_2)  # 支出增加1000
    cursor.execute(sql_3)  # 收入增加2000
except Exception as e:
    conn.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    conn.commit()  # 事务提交
    print('事务处理成功', cursor.rowcount)

# 关闭连接
cursor.close()
conn.close()