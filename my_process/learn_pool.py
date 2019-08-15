from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('run task %s (%s)……' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)  #子进程挂起时间,random产生1以内的随机数
	end = time.time()
	print('task %s runs %0.2f seconds.' % (name, (end - start))) #%0.2f 保留两位小数

if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)  #创建进程池p, 同时执行4个子进程，默认为cpu核数
	for i in range(5):
		p.apply_async(long_time_task, args=(i,)) #创建异步子进程，传入函数及其参数
	print('waiting for all subprocesses done……') #因为是异步子进程，所以子进程执行时可以先打印 这句话
	p.close() #这里意思时关闭p进程池的使用，不能再插入新的元素
	p.join() # 等待所有子进程执行完毕。这里代码不再往下执行，只到子进程p执行完毕
	print('All subprocesses done.')
