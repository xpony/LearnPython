# 写一个计算一元二次方程 ax^2 + bx + c = 0 根的程序
import math  #导入math包， 要用math.sqrt() 来求平方根
def quadratic(a, b, c, Dt):  # 定义计算根的函数
	if Dt == 0:
		return ('方程的解是：', -b / 2*a)
	elif Dt>0:
		res1 = (-b + Dt) / (2*a)
		res2 = (-b - Dt) / (2*a)
		return ('方程的解是：', res1, res2)
	else:
		return '请您检查是否输入正确'

a = int(int(input('请输入方程的a：')))  #让用户输入方程的相关值
b = int(int(input('请输入方程的b：')))
c = int(int(input('请输入方程的c：')))
print('您需要解的方程为：%dx^2 + %dx + %d' % (a,b,c)) 
# 显示要解的方程，用到了字符串的格式化

root_num = b*b - 4*a*c   #计算出dao ta值

if root_num == 0:        # 计算一下方程有几个解，然后顺带计算出dao ta的平方根
	print('方程只有一个解')
	Dt = 0              # Dt 是dao ta 开平方根后的值
elif root_num > 0:
	print('此方程有两个解')
	Dt = math.sqrt(root_num)  # 用计算平方根的函数，计算出dao ta的平方根
else:
	print('对不起，您的方程没有解')
	Dt = -1 

result = quadratic(a, b, c , Dt)  #调用quadratic()函数计算出最终结果
print(result)








