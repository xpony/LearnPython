#用asyncio的异步网络连接来获取sina、baidu和163的网站首页
import asyncio

# @asyncio.coroutine  且将yield from 改为awrit (3.5后的新语法)
async def wget(host):
	print('wget: %s……' % host)
	connect = asyncio.open_connection(host, 80) #创建连接
	reader, writer = await connect #在这里去调用connect 第一个任务等待时，线程去执行第二个任务
	header = 'GET / HTTP/1.0\r\nHost :%s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	await writer.drain()
	while True:
		line = await reader.readline()
		if line == b'\r\n':
			break
		print('%s header > %s' %  (host, line.decode('utf-8').rstrip()))#rstrip()去掉右边空字符
	writer.close() 

loop = asyncio.get_event_loop()
tasks = [wget('www.'+ host) for host in ['sina.com.cn', 'baidu.com', '163.com']] #三个任务
loop.run_until_complete(asyncio.wait(tasks)) 
loop.close()
