#切片（Slice）：
#取一个list或tuple的部分元素是非常常见的操作。比如，取前n个元素，我们可以用循环，但是太麻烦了。如果用切片就会非常简单：
L = [1, 2, 3, 4, 5]
print(L[0:2]) #取前两个元素
print(L[:2])  # 从索引零开始，可以省略
print(L[1:])  # 前
print(L[2:5]) #可以从索引2开始取，取到第五个
print(L[2:])  #默认取完

#既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print(L[-2:])  #从倒数第二个开始，取完
print(L[-2:-1])

print(L[1:3])
print(L[1:2])
#切片操作十分有用。我们先创建一个0-99的数列：
L = list(range(100))  #range(100)表示从0开始生成含100个整数的序列
print(L[:10])   #取出前十个元素
print(L[-10:])  #取出后十个元素
print(L[10:20]) #前十一个到第二十个元素
print(L[:10:2]) #前十个每两个取一个
print(L[::5])   #所有数每五个取一个
print(L[:])     #原模原样复制出一个
print('---------------------------------------------------------------')
#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
t = (1,2,3,4,5)
print(t[:3])  #取出前三个
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
s = 'mahongwei'
print(s[:2])  #取出前两个
### 练习  切除字符串首尾的空格
def trim(str):
	if len(str) == 0:
		print('请输入有效的字符串')
		return str
	elif str[0] == ' ':
			str = str[1:]
			return trim(str)
	elif str[-1] == ' ':
			str = str[0:-1]
			return trim(str)
	return str, len(str)
print(trim('  ma    '))
## if、 elif 后边都要跟条件语句