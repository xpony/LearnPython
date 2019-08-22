#Field类，负责保存数据库表的字段名和字段类型
class Field(object):
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type
	def __str__(self):  #打印此类创建的对象返回的内容
		return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')
class IntegerField(Field):
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')

#创建ModelMetaclass Mode的元类
class ModeMetaclass(type):
	def __new__(cls, name, bases, attrs):  #attr是存储User类方法属性的dict
		if name == 'Model': #排除掉对model的修改
			return type.__new__(cls, name, bases, attrs)
		print('Found model: %s' % name)
		mappings = dict() #创建了一个dict
		for k, v in attrs.items():
			if isinstance(v, Field): #发现属性值类型为Field,就保存这个属性到mappings里
				print('Found mapping: %s ==> %s' % (k, v))
				mappings[k] = v # 保存字段 id --> id的实例
		for k in mappings.keys():
			attrs.pop(k)  #从类属性中删除该Field属性
		attrs['__mappings__'] = mappings #保存到类的属性集合里，形成属性和列的映射
		attrs['__table__'] = name #假设表名和类名一样
		return type.__new__(cls, name, bases, attrs)

# 创建基类 Model
class Model(dict, metaclass=ModeMetaclass):
	def __init__(self, **kw): #接受关键字参数
		super(Model, self).__init__(**kw)

	def __getattr__(self, key): #这两个函数为了处理关键字参数
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)
	def __setattr__(self, key, value): #拿关键字参数组成的dict的value
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items(): #这里都是类的属性
			# print('k = %s' % k)
			# print('v = %s' % v.name)
			fields.append(v.name)  # v是id对象 id.name  id.cloumn_type
			params.append('?')
			args.append(getattr(self, k)) #getattr()拿的是实例的属性值
		sql = 'insert into %s (%s) value (%s)' % (self.__table__, ','.join(fields), ','.join(params))
		print('SQL:%s' % sql)
		print('ARGS: %s' % str(args))

class User(Model):
	id = IntegerField('id')
	name = StringField('username')  #这些都是user类的属性
	email = StringField('email')
	password = StringField('password')

u = User(id=12345, name='xpony', email='test@email', password='my-pwd')
u.save()


