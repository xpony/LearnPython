#生成器（generator）：
#过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
#而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要
#访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
#所以，如果列表元素可以按照某种算法推算出来，那我们不可以在循环的过程中不断推算出后续的元素？
#这样就不必创建完整的list，从而节省大量的空间。
#在Python中，这种一边循环一边计算的机制，称为生成器：generator。


#创建generator的方法。

#第一种：只要把一个列表生成式的[ ]改成( )，就创建了一个generator
L = [x * x for x in range(10)] # L是一个list
print(L)
g = (x * x for x in range(10))  # g是一个generator
print(g)


#next( ) 函数：   获得generator的下一个返回值 
print(next(g))
print(next(g))

#使用for循环，因为generator也是可迭代对象：
for n in g:
	print(n)

#第二种： 如果推算的算法比较复杂，还可以用函数来实现。
#例如：著名的斐波拉契数列（Fibonacci）1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
	n, a, b = 0, 0, 1  
	while max > n:	  
		yield b    # print(b) 改为 yield b 此函数就是个generator
		a, b = b, a + b  
		n = n + 1
	return 'done'

print(fib(6))

#调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
g = fib(6)
print(next(g))
print(next(g))
print(next(g))

#可以直接使用for循环来迭代：
for n in fib(5):
	print(n)


#但是用for循环调用generator时，发现拿不到generator的return语句的返回值(done)。
#如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(4)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break







