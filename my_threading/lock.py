import time, threading

lock = threading.Lock()  #生成一把锁
balance = 0  #你的银行存款

def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n #先存后取，结果因该是0

def run_thread(n): # 线程要执行的代码
	for i in range(10000000):
		lock.acquire() #先要获得锁
		try:
			change_it(n) #随便改吧
		finally:
			lock.release() #改完了要释放锁

t1 = threading.Thread(target=run_thread, args=(5,)) #创建线程t1
t2 = threading.Thread(target=run_thread, args=(8,)) #创建线程t2
t1.start() 
t2.start()
t1.join()  
t2.join()
print(balance)  #// 当循环一百万次时 结果不再是 0






