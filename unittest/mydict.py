# 编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问
class Dict(dict):
	def __init__(self, **kw):
		super().__init__(**kw)  #去父类里初始数据

	def __getattr__(self, key):  #通过属性调用时，返回相应的值或抛出错误
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'dict' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):  #通过属性添加
		self[key] = value


d = Dict(a=1, b=2)
print(d)
print(d['a'])
print(d.a)	   #可以通过属性访问了	 

d.c = 3
print(d.c)     #可以通过属性添加了
print(d)





