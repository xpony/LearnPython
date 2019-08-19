#hello.py
#HTTP处理函数
def application(emviron, start_repose):
	start_repose('200 OK', [('Content-Tyte', 'text/html')])#发送HTTP响应
	body = '<h1>Hello, %s</h1>' % (emviron['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')] #返回网页内容


