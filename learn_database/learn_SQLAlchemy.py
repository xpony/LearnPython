from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()   #创建对象的基类
class User(Base): #创建User对象
	__tablename__ = 'user'
	#表的结构
	id = Column(String(20), primary_key=True)
	name = Column(String(20))

#初始化数据库连接。  用一个字符串表示连接信息：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:root123@localhost:3306/test')
DBSession = sessionmaker(bind=engine) #创建DBSession类

#下面向数据库添加一条记录
session = DBSession() #创建session对象
new_user = User(id='5', name='Bob') #创建新User对象
session.add(new_user) #添加到session
session.commit() #提交即保存到数据库
session.close() #关闭session

#下面查询数据的记录
session = DBSession() #创建session
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
print('name:', user.name) #打印对象的name属性
session.close()

