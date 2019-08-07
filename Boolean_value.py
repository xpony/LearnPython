#一个布尔值只有True、False两种值（注意大小写）,在Python中，可以直接用True、False表示布尔值
print(True)
print(False)
#布尔值可以用and、or和not运算。
# and运算是与运算，只有所有都为True，and运算结果才是True
print(True and True) #输出为True 
print(True and False) #输出为False

# or运算是或运算，只要其中有一个为True，or运算结果就是True
print(True or False) # 输出为True
print(True or True) # 输出为True 

# not运算是非运算，它是一个单目运算符，把True变成False，False变成True：
print(not True) #输入为False

# 布尔值经常用在条件判断中，比如：
age = int(input('请输入你的年龄：'))  # input()默认返回字符串类型，int()讲字符串转换成整数类型
if age >= 18:
	print('adult')
else:
	print('teenager')