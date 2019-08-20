#协程 
def consumer():  #是一个生成器
	r = ''
	while True:
		s = yield r #接收参数赋给s 返回的是r
		if not s:
			return
		print('[CONSUMER] consumer %s……' % s)
		r = '200 OK'

def prodect(c):
	c.send(None) #启动生成器 第一次要发None才能启动
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODECT] prodecing %s……' % n)
		r = c.send(n) 
		print('[PRODECT] consumer return:%s' % r)
	c.close()  #关闭生成器

c = consumer()
prodect(c)
