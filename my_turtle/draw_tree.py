#画一棵树
from turtle import *

colormode(255) # 设置色彩模式是RGB:
lt(90) #左转

lv = 14
l = 120
s = 45

width(lv)

r = 0    # 初始化RGB颜色:
g = 0
b = 0
pencolor(r, g, b)

penup() #抬起画笔
bk(l)   #后退
pendown() #落下画笔
fd(l)  #前进

def draw_tree(l, level):
    global r, g, b
    w = width()  # 保存当前画笔宽度
    width(w * 3.0 / 4.0)  # 画笔变窄
    r = r + 1      # 设置颜色:
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l
    lt(s) #左转
    fd(l) #前进

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)
    
    width(w)# 恢复之前的画笔宽度

speed(0) #速度最快  速度档： 1 3 6 10 0 
draw_tree(l, 4)
done()