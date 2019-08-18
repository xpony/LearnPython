import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP类型的socket
#不用调用connect()，直接发送即可
for data in [b'xpony', b'wanmeng', b'123']:
	s.sendto(data, ('127.0.0.1', 9999)) #发送数据
	print(s.recv(1024).decode('utf-8')) #接收数据 客户端依然用recv()接收
s.close()







