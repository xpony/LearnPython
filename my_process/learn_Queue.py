from multiprocessing import Process, Queue #大写开头的一般都是个类
import os, time, random

#写数据进程执行的代码
def write(q):
	print('process to write:%s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('put %s to queue……' % value)
		q.put(value)  #往Queue里写入数据
		time.sleep(random.random())  #进程挂起一下

#读数据进程执行的代码
def read(q):
	print('process to read: %s' % os.getpid())
	while True:
		value = q.get()  #从Queue里读取数据
		print('get %s from queue.' % value)

#父进程执行的代码	
if __name__=='__main__':
	q = Queue()  #父进程创建Queue
	pw = Process(target=write, args=(q,)) #创建子进程pw,并把Queue传给它
	pr = Process(target=read, args=(q,))  # 与上同理
	pw.start()  #启动子进程 pw, 写入
	pr.start()  #启动子进程 pr, 读取
	pw.join()   #等待pw结束	
	pr.terminate() #pr进程是死循环，需要强行终止











