import asyncio

#把generator标记为coroutine类型
async def hello(): #新语法后，表示这是个异步函数
	print('hello,world!')
	r = await asyncio.sleep(1) #异步调用asyncio.sleep(1)
	print('hello,again!')

loop = asyncio.get_event_loop()#获取Eventloop
loop.run_until_complete(hello()) #执行coroutine(执行协程)
loop.close()  #关闭






