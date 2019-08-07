#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['yangfan','zhaotao','mahongwei'] # 创建一个list
print(classmates)

cla_num = len(classmates)  #用len()函数可以获得list元素的个数：
print(cla_num)
print(classmates[0]) #用索引来访问list中每一个位置的元素，记得索引是从0开始的

print(len(classmates) - 1) # 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1

print(classmates[-1]) #如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(classmates[-2]) #倒数第二个元素

#list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('lihu')
print(classmates)

#也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1,'zhangmao')
print(classmates)

#要删除list末尾的元素，用pop()方法
classmates.pop()
print(classmates)

#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(2)
print(classmates)

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'heqishan'
print(classmates)

#list里面的元素的数据类型也可以不同，比如:
L = ['China',123,True]
print(L)

#list元素也可以是另一个list，比如：
s = ['python','java',['html','css'],'php']
print(s)
print(len(s))
#s是一个二维数组，要拿到html，可以这样写
print(s[2][0])

#如果一个list中，一个元素也没有就是个空list， 长度为0