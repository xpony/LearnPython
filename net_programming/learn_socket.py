import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建一个socket
s.connect(('www.sina.cn', 80)) #建立连接
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接收数据
buffer = []
while True:
    d = s.recv(1024)  #每次最多接收1k字节
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()# 关闭连接:

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
#把收到的数据写入文件
with open('sina.html', 'wb') as f: #创建了一个文件，并把html写入
    f.write(html)



