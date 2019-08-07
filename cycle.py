#一  for… in 循环，依次把list或tuple中的每个元素迭代出来，例如：
names = ['mahongwei','zhaotao','yangfan']
for name in names:
	print(name)
#利用循环做叠加运算
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x
print(sum)

#range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
L = list(range(5)) #比如range(5)生成的序列是从0开始小于5的整数
print(L)

#现在计算0到100的整数累计和：

sum = 0
for x in range(101):
	sum = sum + x
print(sum)

#二  while循环，只要条件满足，就不断循环，条件不满足时退出循环。
#计算100以内所有奇数之和，可以用while循环实现：
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)

#break语句，break语句可以提前退出循环。
n = 1
while n <= 100:
	if n > 10:
		break  #break语句会结束当前循环
	print(n)
	n = n + 1
print('END')
#continue语句，可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。

#如果只想打印1-10的奇数，可以用continue语句跳过某些循环：
n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0:
		continue    #n为偶数时，continue 直接跳过了这次循环，进行下一次循环
	print(n)
#可见continue的作用是提前结束本轮循环，并直接开始下一轮循环。