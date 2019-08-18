#生成字母验证码图片
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

#随机字母
def rndChar():
	return chr(random.randint(65, 90))

#随机颜色1:
def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#随机颜色2：
def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 240 #图片大小
height = 60
im = Image.new('RGB', (width, height), (255, 255, 255)) #生成新图片
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36) #创建font对象  字体位置需要填绝对路径
draw = ImageDraw.Draw(im) #创建draw对象
for x in range(width): #填充每一个像素
	for y in range(height):
		draw.point((x, y), fill=rndColor())
for t in range(4):  # 输出文字
	draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
im = im.filter(ImageFilter.BLUR)
im.save('code.jpg')
#不懂的地方就看官方文档




