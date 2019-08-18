#server
import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建一个socket
s.bind(('127.0.0.1', 9999)) #绑定IP和端口
s.listen(5) #开始监听，等待连接的最大数量为5
print('waiting for connection……')

def tcplink(sock, addr):
	print('Accept new connection for %s:%s' % addr)
	sock.send(b'welcom!')#连接建立后，服务器先发一条消息，然后等待客户端数据
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('connection from %s:%s cloed.' % addr)

while True:
	sock, addr = s.accept() #接受一个新的连接,返回一个客户端的连接和其地址
	#创建一个新线程来处理TCP连接
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()






