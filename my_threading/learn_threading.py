import time, threading

#新线程执行的代码
def loop():
	print('thread %s is running……' % threading.current_thread().name) # 当前线程的名字
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(1) #挂起一秒
	print('thread %s end.' % threading.current_thread().name)

#主线程执行的代码
print('thread %s is running……' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread') #创建了一个新线程，它要执行的函数和它的名字
t.start() #启动线程
t.join()  #等待线程执行完毕
print('thread %s ended.' % threading.current_thread().name)






