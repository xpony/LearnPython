#使用@property的小练习
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object): #创建一个类
    @property            #读取wdith属性
    def width(self):
        return self._width
    @width.setter       #写入width属性
    def width(self, value):
        self._width = value

    @property            #读取height属性
    def height(self):
        return self._height
    @height.setter       #写入height属性
    def height(self, value):
    	self._height = value

    @property            # 这是一个只读属性
    def resolution(self):
    	return self._width * self._height
    
iphone = Screen()  #生成一个实例
iphone.width = 30   
iphone.height = 100
print(iphone.resolution)