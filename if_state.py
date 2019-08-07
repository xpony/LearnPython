age = 20
if age >= 18:
	print('you are adult')
else:
	print('you are a little friend')

#可以用elif做更细致的判断：
age = int(input('你多大啦：'))
if age >= 18:
	print('adult')
elif age >= 10:
	print('teenager')
else:
	print('kid')
#elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
#if <条件判断1>:
#    <执行1>
#elif <条件判断2>:
#    <执行2>
#elif <条件判断3>:
#    <执行3>
#else:
#    <执行4>
x = (1,2)           #这里x 给定义了一个tuple（元组）
if x:
	print('True')   #if判断条件还可以简写,就像这样。嘿嘿
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False