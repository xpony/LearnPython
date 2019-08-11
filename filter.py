#filter( )函数 用于过滤序列。同样接收一个函数和一个序列，把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素。和map()一样返回的是Iterator

#例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
	return n % 2 == 1   # 判断是否为奇数
num = filter(is_odd, [1, 2, 3, 4, 5, 6, 10])
print(list(num))

#把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
	return s and s.strip() #strip()去除字符串首尾空格，对单个空格作用后，bool值为False
s = filter(not_empty, ['A', 'B', '', None, '    '])  # None的bool值为False
print(list(s))


#用filter求素数
#构造一个从3开始的奇数序列
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n     #这是个一个生成器函数

#生成器函数可以用for循环来不断输入结果，也可以生成个对象，然后用next()函数返回下个值
#g = _odd_iter()
# print(next(g))

#定义一个帅选函数
def _not_divisible(n):
	return lambda x: x % n > 0

# 再定义一个生成器，不断返回下一个素数
def primes():
	yield 2
	it = _odd_iter()  #生成一个对象，其包括大于3的奇数
	while True:
		n = next(it)  #返回序列的第一个数
		yield n   #返回素数
		it = filter(_not_divisible, it)  # 构造新序列

for n in primes():   # 打印100以内的素数:
	if n < 100:
		print(n)
	else:
		break



# 练习 数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

#教训！： 命名变量时千万不要用一些内置函数名，否则找找bug找到你哭
# 自然正整数生成函数
def _add_nums():
	n = 10
	while True:
		yield n
		n = n + 1

# 判断是否为回数
def number_h(n):
	return str(n) == str(n)[::-1]

numbers = _add_nums() #生成自然是想序列的对象

nums = filter(number_h, numbers) # 生成回数序列

for n in nums:  #打印出1000以内的回数
	if n < 1000:
		print(n)
	else:
		break