import threading
import asyncio

@asyncio.coroutine
def hello():
	print('hello,world! (%s)' % threading.currentThread())
	yield from asyncio.sleep(1)
	print('hello,again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()] #两个coroutine
loop.run_until_complete(asyncio.wait(tasks)) #同一线程异步执行两个任务
loop.close()






