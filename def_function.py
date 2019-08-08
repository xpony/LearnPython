#自定义一个求绝对值的my_abs函数为例：\
# 方式 依次写 def  函数名  括号(及参数)   ：
def my_abs(x):
	if x >= 0:
		return x   #return 返回函数值
	else:
		return -x
print(my_abs(-3))
#注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。

#如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，
#可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，
#注意abstest是文件名

#空函数 如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
	pass
#pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，
#就可以先放一个pass，让代码能运行起来。

# 检查参数  用内置函数 isinstace()
def my_Newabs(x):
	if not isinstance(int, float):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x
#print(my_Newabs('12'))

#返回多个值
import math  #导入math包，后续代码就可以使用math包里的sin、cos等函数了

def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny

print(move(100, 100, 60, math.pi/6))

#但其实这只是一种假象，Python函数返回的仍然是单一值
r = move(100, 100, 60, math.pi/6)
print(r)

# 返回值其实是一个tuple (151.96152422706632, 130.0)
#在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
#list，set，dict 都类似可以这样赋值给变量






