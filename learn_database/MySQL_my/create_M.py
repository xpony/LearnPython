import mysql.connector #导入MySQL驱动

#连接数据库
conn = mysql.connector.connect(user='root', password='root123', database='test')
cursor = conn.cursor() #创建游标
#创建一个user表
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#插入一行记录
cursor.execute('insert into user (id, name) values (%s, %s)', ['3', 'red'])
print(cursor.rowcount) #打印一下插入的行数
conn.commit() #提交事务
cursor.close()# 关闭游标

#运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id =%s', ('1',)) #MySQL的占位符是%
values = cursor.fetchall() #获取查询结果
print(values)
cursor.close()
conn.close() #关闭连接

