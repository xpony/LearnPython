import threading

local_school = threading.local() #创建全局的threadlocal对象

def process_std():
	std = local_school.student  #获取当前线程关联的student
	print('hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
	local_school.student = name #把当前线程的名字绑定到local_shool对象的student属性上
	process_std()

t1 = threading.Thread(target=process_thread, args=('Alice',))
t2 = threading.Thread(target=process_thread, args=('Xpony',))
t1.start()
t2.start()
t1.join()
t2.join()




