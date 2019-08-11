#map( )函数:  接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用
#到序列的每个元素，并把结果作为新的Iterator返回。

#我们要把f(x)=x2这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现
def f(x):
	return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
#注意：list()函数可以直接作用于生成器or迭代器，把整个序列都计算出来并返回一个list。


#我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，
#比如，把这个list所有数字转为字符串：
s = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(s))


#reduce( )函数:  同样接收一个函数，一个序列，将函数作用于序列上。但注意，
#接收的这个函数必须接收两个参数，reduce把结果继续与序列的下一个元素做累积计算

#比方说对一个序列求和，就可以用reduce实现：
from functools import reduce  #  reduce要引入后才能使用
def add(x, y):
	return x + y
sum = reduce(add, [1, 3, 5, 7, 9]) ##reduce返回的是值，map返回是iterator
print(sum)


#把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn(x, y):
	return x * 10 + y
num = reduce(fn, [1, 3, 5, 7, 9])
print(num)



#，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，
#配合map()，我们就可以写出把str转换为int的函数：
def fn(x, y):
	return x * 10 + y
def char2num(s):
	digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
	return digits[s]
num = reduce(fn, map(char2num, '2019'))
print(num)


#可以用lambda函数进一步简化成：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('1997'))
#lambda函数  冒号前后    接收的参数 ：return的值


#练习1：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def name(x):
	return x.capitalize()
names = map(name, ['adam', 'LISA', 'barT'])
print(list(names))

#练习3：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def fn(x, y):
	return x * 10 + y
def str2float(s):
	digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
	return digits[s]

str = '123.4346'
L = [x for x in str]
for i, value in enumerate(L):  #可以返回list的索引-元素对
	if value == '.':
		mark = i + 1           # 查找字符串里小数点的位置

mark = len(str) - mark   
mark = pow(10, mark)  # pow(x, y) 返回 x的y次方
					  # 计算出百千位

str = str.replace('.', '')  # 去掉字符串里的小数点

num = reduce(fn, map(str2float, str))
print(num / mark)