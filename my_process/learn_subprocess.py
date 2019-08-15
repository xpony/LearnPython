import subprocess   #引入subprocess模块
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])   # 可以换成ping命令
print('Exit code:', r)     # r会有一个返回值

print('-----------分割线----------------------')

#如果子进程还需要输入，则可以通过communicate()方法输入：
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄

output, err = p.communicate(b'set q=mx\npython.org\nexit\n')  #是个tuple类型

print(output.decode('utf-8', errors='ignore'))
print('Exit code:', p.returncode)
#print((p.communicate()))






