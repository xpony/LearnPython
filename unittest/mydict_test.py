#编写单元测试，要引入unittest模块
import unittest
from mydict import Dict   #从mydice.py文件里导入Dict类

class TestDict(unittest.TestCase): #编写一个测试类，从unittset.TestCase继承
	
	def setUp(self):      #每调用一个测试方法前后会分别执行这两个方法
		print('setUp……')  #可以用来启动和关闭数据库

	def tearDown(self):
		print('tearDown……')

	def test_init(self):          #初始化数据的方法
		d = Dict(a=1, b='test')
		self.assertEqual(d.a, 1)  #断言  d.a 是 1
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):       #测试通过key赋值
		d = Dict()
		d['key'] = 'value' 
		self.assertEqual(d.key, 'value')  #断言

	def test_attr(self):       #测试通过属性赋值
		d = Dict()
		d.key = 'value'    
		self.assertTrue('key' in d)  
		self.assertEqual(d['key'], 'value')

	def keyerror(self):		#断言抛出指定类型的错误，当访问不存在的key时   
		d = Dict()			
		with self.assertRaises(KeyError):  #with:执行完后关闭了这个错误，使后边的程序还能执行
			value = d['empty']

	def test_attrerror(self):   
		d = Dict()
		with self.assertRaises(AttributeError): #断言抛出指定类型的错误
			value = d.empty

#以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
#unittest.TestCase提供了很多内置的条件判断,最常用的断言就是assertEqual()：


if __name__ == '__main__':  # 命令行执行单元测试
	unittest.main()






