##位置参数
#计算x^2的函数：
def power(x):   # x 是一个位置参数
	return x * x
print(power(3)) # 当我们调用power()时，必须有且仅传入一个参数

# 再定义个可以求x的n次方的函数
def power2(x, n):
	s = 1
	while n > 0:
		s = s * x
		n = n - 1
	return s
print(power2(3,3))
# power2(x, n)函数有两个参数：x和n，这两个参数都是位置参数，
# 调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。

##默认参数
# 由于我们经常计算的2次方，所以，完全可以把第二个参数n的默认值设定为2：
def power3(x, n=2):
	s = 1
	while n > 0:
		s = s * x
		n = n - 1
	return s
print(power3(3,3))
print(power3(3))  #相当于调用了 power2(3,2) 
#默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
#一是必选参数在前，默认参数在后，否则Python的解释器会报错（why:因为按顺序赋值）
#二是当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#有多个默认参数时，调用的时候，既可以按顺序提供默认参数，python会按顺序赋值，没有提供的参数，使用默认值
#也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
#例如：enroll('Adam', 'M', city='Tianjin')


#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，例如：
def add_end(l=[]):
	l.append('end')
	return l
print(add_end([1,2,3])) #当你正常调用时，结果似乎不错

print(add_end()) #当你使用默认参数调用时，一开始结果也是对的
print(add_end()) #但是，再次调用add_end()时，结果就不对了,多出了一个end
#很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
#原因：Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
#每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
##定义默认参数要牢记一点：默认参数必须指向不变对象！

##可变参数：
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc(1,2,3))
print(calc(1,2,3,4))
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，
#因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数。
nums = [1,2,3]
print(calc(nums[0],nums[1],nums[2])) #已经有一个list或者tuple，可以这样传入
#种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，
#把list或tuple的元素变成可变参数传进去：
print(calc(*nums))#nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

##关键字参数  (dict参数，可以传入一个dict)
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def person(name, age, **kw):  #kyeword(关键字)
	print('name:', name, 'age:', age, 'other:', kw)
person('mahongwei', 22)  # 只传入必选参数

person('yangfan', 23, jobyear=23) #也可以传入任意个数的关键字参数
person('xpony', 33, city='xi an', weight=120)
#键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
#但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，
#除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

#与可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('you', 11, **extra)  #可变参数是一个*，关键字参数是**
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
#注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

## 命名关键字参数
#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
#至于到底传入了哪些，就需要在函数内部通过kw检查。
def person(name, age, **kw):

	if 'city' in kw:
		# 有city参数
		pass
	if 'job' in kw:
		# 有job参数
		pass
	print('name:', name, 'age:', age, 'other:', kw)
person('jack', 24,  addr='chaoyang', zipcode=12345) #调用者仍可以传入不受限制的关键字参数

#如果要限制关键字参数的名字，就可以用命名关键字参数，
#例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job): # 定义命名关键字参数时，要用一个分隔符*，*后边的参数视为命名参数
	print(name, age, city, job)
person('haha', 100, city='jinyuan' , job='cpu')
#只能传入，已经命名的关键字参数，多传和少传会报错。 顺序可以打乱，因为有名字，可以自己查找

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job): #可变参数后的默认为了命名关键字参数
	print(name, age, args, city, job)
person('xixi', 120, (1,3,5), city='guyuan', job='jialidun')
# 命名关键字参数，必须传入参数名，否则会报错，因为没有名字python会认为是位置参数，但其实并没有定义这个位置参数。

#命名关键字参数可以添加默认值，从而简化调用
def person(name, age, *, city='xian', job):
	print(name, age, city, job)
person('mahongwei', 22, job='hacker')

#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
#如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：

print('---------下边是组合参数------------')
##参数组合
#在Python中定义函数，可以用位置参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
#但是请注意，参数定义的顺序必须是：位置参数、默认参数、可变参数、命名关键字参数和关键字参数。
print('组合参数顺序：\n位置参数、\n默认参数、\n可变参数、\n命名关键字参数、\n关键字参数')
#比如定义一个函数，包含上述若干种参数：
def f1(a, b, c=0, *args, **kw):
	print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
f1(1,2,)
f1(1,2,5)
f1(1, 2, 3, 'a', 'b', x=99)

#最神奇的是通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4, 4)    # 定义一个tuple
kw = {'d': 99,  'x': '#'}  #定义一个dict
f1(*args,  **kw)  

# 计算任意几个数的乘积
def product(*args): #设置一个可变参数
	sum = 1
	for n in args:
		sum = sum * n 
	return sum
l = [1,2,3,4]
print(product(*l))  
