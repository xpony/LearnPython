# task_master.py
import random, time, queue
from multiprocessing.managers import BaseManager
#from multiprocessing import freeze_support

task_queue = queue.Queue() #任务发送队列
result_queue = queue.Queue() #结果接收队列

class QueueManager(BaseManager): #从BaseManager继承的QueueManager类
	pass

def t1():
	return task_queue
def t2():
	return result_queue

def test():
	#把两个本地队列注册到网络上，并关联名字
	QueueManager.register('get_task_queue', callable=t1)
	QueueManager.register('get_result_queue', callable=t2)

	manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc') #绑定端口，设置验证码
	manager.start() #启动网络
	task = manager.get_task_queue() #获得可以通过网络访问的queue对象
	result = manager.get_result_queue() 

	for i in range(10): #放几个任务进去
		n = random.randint(0, 10000) #产生0到10000的随机整数
		print('put task %d……' % n)
		task.put(n)  

	print('try get results……')
	for i in range(10):
		r  = result.get(timeout=10)
		print('result: %s' % r)

	manager.shutdown() #关闭网络
	print('master exit.')


if __name__=='__main__':
#	freeze_support()  可以不要这个，只需要把进程池相关代码放在__name__=='__main__'
	test()












