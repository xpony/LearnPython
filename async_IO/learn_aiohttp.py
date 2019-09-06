#aiohttp  单线程+coroutine实现多用户的高并发支持
import asyncio
from aiohttp import web

async def index(request):#reques？
	await asyncio.sleep(1)
	return web.Response(body=b'<h1>Index</h1>', content_type='text/html')

async def hello(request):
	await asyncio.sleep(1)
	text = '<h1>hello, %s!</h1>' % request.match_info['name'] #传入的参数从request上获取
	return web.Response(body=text.encode('utf-8'), content_type='text/html')

async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index) #添加路由
	app.router.add_route('GET', '/hello/{name}', hello)
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 5000) #创建一个服务
	print('server started at http://127.0.0.1:5000……')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop)) #init()本身也是一个coroutine
loop.run_forever()








