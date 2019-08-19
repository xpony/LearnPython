#创建
import sqlite3 #导入SQL驱动

#连接到数据库
conn = sqlite3.connect('test.db') #如果文件不存在，会自动创建在当前目录
cursor = conn.cursor() #创建一个游标
#执行SQL语句，创建一个user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#插入一条记录
cursor.execute('insert into user (id, name) values (\'1\', \'xpony\')')
print(cursor.rowcount) #获得插入的行数
cursor.close() #关闭游标
conn.commit() #提交事务
conn.close() #关闭连接