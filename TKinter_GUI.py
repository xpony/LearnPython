#一个简单的GUI程序，可以输入并点击按钮弹出输入内容
from tkinter import * #导入TKinter包所有内容
import tkinter.messagebox as messagebox  # 用来创建消息输入窗口
#从Frame派生一个Applicatioin
class Application(Frame):
	def __init__(self, mster=None):
		Frame.__init__(self, mster)
		self.pack() #把自己变成Frame内的一个窗口
		self.createWidgets() #调用自己的方法，创建好需要的窗口

	def createWidgets(self): #小部件布局顺序，由下面代码顺序决定
		self.helloLabel = Label(self, text='请在输入') # 创建一个标签
		self.helloLabel.pack() #把这个窗口加入到父容器中，并实现布局
		self.nameInput = Entry(self) # 输入框
		self.nameInput.pack()
		self.quitButton = Button(self, text='Hello', command=self.hello) #点击这个按钮触发hello
		self.quitButton.pack() #把这个窗口加入到父容器中

	def hello(self):
		name = self.nameInput.get() or 'world' #先获取self.nameInput里的值，没有就使用‘world’
		messagebox.showinfo('message', 'hello, %s' % name) #显示消息
#实例化Application
app = Application()
print(app)
app.master.title('First App')#设置窗口标题，windows下好像没有效果
app.mainloop() #让窗口一直出现