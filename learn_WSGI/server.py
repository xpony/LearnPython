#server.py  负责启动WSGI服务器，加载application函数
from wsgiref.simple_server import make_server
from hello import application        #导入我们自己编的application函数

#创建一个服务器，IP地址为本机，端口8000，处理函数application
httpd = make_server('127.0.0.1', 8000, application)
print('server HTTP on port 8000……')
httpd.serve_forever() #开始监听HTTP请求




