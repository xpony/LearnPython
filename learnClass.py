
#类和实例
class Student(object): #创建一个类 一般用大写字母开头表示类

	def __init__(self, name, score): #初始化实例属性
		self.name = name
		self.score = score

	def print_score(self):    # 创建实例所拥有的方法
		print('%s: %d' % (self.name, self.score))

xpony = Student('xpony', 100) #通过类创建一个实例

print(xpony.name) # 实例的名字
print(xpony.score)  #实例的分数
xpony.print_score() #实例的方法


print('---------------一个更加有趣的例子-----------------')

class Person(object):  #创建一个人的类

# 这里就是初始化你将要创建的实例的属性
    def __init__(self, hight, weight, age):
        self.hight = hight
        self.weight = weight
        self.age = age

# 定义你将要创建的实例所有用的技能，也就是方法
    def paoniu(self):
        print('你拥有泡妞的技能')

    def eat(self):
        print('you can eat')

# 用类开始创建实例
zhangsan=Person(170, 50, 29)
lisi = Person(175, 100, 30)

#你的实例展示它的属性
print(zhangsan.hight, zhangsan.age)

# 你的实例开始使用它的技能
zhangsan.paoniu()
lisi.eat()
