#海龟绘图 ,绘制一个长方形
from turtle import * 
width(4) #设置笔刷宽度

forward(200) #前进200
right(90) #右转90度 ，不设置笔刷颜色默认为黑色

pencolor('red') #设置笔刷颜色
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)

#done() #调用done()使得窗口等待被关闭，否则将立即关闭

#绘制五角星
pencolor('red')
def drawStart(x, y):
	pu()
	goto(x, y)
	pd()
	seth(0) #set heading 0
	for i in range(5):   #连续画了五笔
		fd(40)   #前进
		rt(144)  #右转
for x in range(0, 200, 50): #0, 50, 100, 150 画五角星的x坐标起点
	drawStart(x, -50)

done()
