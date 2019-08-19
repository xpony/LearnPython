import sqlite3

conn = sqlite3.connect('test.db') #连接数据库
cursor = conn.cursor()#创建游标
#执行SQL语句
cursor.execute('select * from user where id=?', ('1',)) #?占位符，有几个占位符就需要几个参数
values = cursor.fetchall() #获得查询结果
print(values) #打印查询结果
cursor.close() #关闭游标
conn.close() #关闭连接



