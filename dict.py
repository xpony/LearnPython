#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，
#使用键-值（key-value）存储，具有极快的查找速度。
d = {'mahongwei':89, 'yangfan':'A', 'zhaotao':100}  # dict用的是{花括号}
print(d['yangfan'])
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['zhangmao'] = 99
print(d)
#由于一个key只能对应一个value，所以多次对一个key放入value，后面值会把前面值替换掉

#如果key不存在，dict就会报错
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
print('chengyingqi' in d)
#是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('heqishan'))
print(d.get('heqishan', 0)) #如何heqishan,不在字典里，返回0

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('mahongwei')
print(d)	

#set  set和dict类似，也是一组key的集合，
#但不存储value。由于key不能重复，所以，在set中，没有重复的key。

#要创建一个set，需要提供一个list作为输入集合：
s =  set([1,2,3])
print(s)   #set相当于是一个没有value 的 dict

#重复元素在set中自动被过滤：
s =  set([1,2,3,2,3,4])
print(s)
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(8)
print(s)

#通过remove(key)方法可以删除元素：
s.remove(1)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)  # 交集
print(s1 | s2) 	# 并集

#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，
#所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，
#也就无法保证set内部“不会有重复元素”。	

#议不可变对象
#我们知道，str是不变对象，而list是可变对象。
#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c','b','a']
print(a)
a.sort()  # sort()方法 对元素进行正常排序
print(a)  # 改变了a中的元素
#而对于不可变对象，比如str，对str进行操作呢：
s = 'abc'
ss = s.replace('a','A')  #返回了一个新的字符串对象，原来的并没有改变
print(s)
print(ss)
#所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
#相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
