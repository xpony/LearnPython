import socket

#SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999)) #绑定端口

#不需要调用listen()方法，而是直接接收来自任何客户端的数据
print('bind UDP on 9999……')
while True:
	data, addr = s.recvfrom(1024) #recvfrom 接收客服端数据
	print('received from %s:%s.' % addr)
	s.sendto(b'hello, %s!' % data, addr)
#这里没有用多线程，因为这个例子很简单





