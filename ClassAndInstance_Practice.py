class Student(object):
    def __init__(self, name, gender):
        self.__name = name      #私密数据，外部无法直接访问
        self.__gender = gender   #私密数据，外部无法直接访问

    def get_gender(self):    # 获取数据的方法
        	print(self.__gender) 

    def set_gender(self, gender):     # 修改数据的方法  做了参数检查
        	if gender == '男' or gender == '女':
        		self.__gender = gender
        	else:
        		raise ValueError('bad gender')
xpony = Student('xpony', '男')

xpony.get_gender()         
xpony.set_gender('女')
xpony.get_gender()         
