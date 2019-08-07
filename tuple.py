#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
classmates = ('yanfan','zhaotao','mahongwei') # tuple用（）定义
print(classmates)
#现在 classmates 不能改变了，它没有append(), insert(), pop()这样的方法。
#获取元素方式和list一样，classmates[0], classmates[-1],但不能赋值成另外的元素
#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

#当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
t = (1,2)
print(t)
#如果要定义一个空的tuple，可以写成()
t = ()
#但是，要定义一个只有1个元素的tuple，如果你这么定义：
t = (1)  # 其结果是 1 这个数。因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
#因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1

#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print(t)



#可变的tuple
t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
#	表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，
#	而是list的元素。tuple一开始指向的list并没有改成别的list，
#	所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
#	即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，
#	但指向的这个list本身是可变的！