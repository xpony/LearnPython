#task_work.py
import time, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager): #创建类似的QueueManager
	pass

#这个QueueManager只从网络上获取queue,所以注册时只提供名字
QueueManager.register('get_task_queue') 
QueueManager.register('get_result_queue')
server_addr = '127.0.0.1' #服务器地址，也就是运行task_master的机器
print('connect to server %s……' % server_addr)
#创建连接网络
manager = QueueManager(address=(server_addr, 5000), authkey=b'abc') 
manager.connect() #开始连接

task = manager.get_task_queue() #获取暴露在网络上的queue对象
result = manager.get_result_queue()

#从task队列获取任务，并把结果写入result队列
for i in range(10):
	try:
		n = task.get(timeout=10)  #timeout 是等待时间
		print('run task %d * %d……' % (n, n))
		r = '%d * %d = %d' % (n, n, n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty')

print('worker exit.') #处理结束




