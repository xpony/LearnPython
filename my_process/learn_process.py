from multiprocessing import Process  #引入Process类
import os


def run_proc(name):
	print('run child process %s (%s)……' % (name, os.getpid()))  #子进程要执行的代码


if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target=run_proc, args=('test',)) #用Process类创建一个子进程实例
	print('child process will start.')
	p.start() # 启动子进程
	p.join()  # 等待子进程结束
	print('child process end.')  #子进程执行完了，就执行这句



