from email.mime.text import MIMEText #构造邮件
from email.header import Header 
from email import encoders
from email.utils import parseaddr, formataddr
import smtplib #发送邮件

def _format_addr(s): #这个函数来格式化邮箱地址
	name, addr = parseaddr(s) 
	return formataddr((Header(name, 'utf-8').encode(), addr)) #格式化

#填写发件信息
from_addr = input('你的邮箱：')
password = input('邮箱密码：') #这里的密码是开启服务后邮箱服务商提供的效验码
to_addr = input('对方邮箱：')
smtp_server = input('SMTP server:') #输入SMTP服务器地址

#构造纯文本邮件
msg = MIMEText('hello, send by python……', 'plain', 'utf-8')
msg['From'] = _format_addr('python爱好者<%s>' % from_addr) #增加了msg的属性
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

#准备发送邮件
server = smtplib.SMTP(smtp_server, 25) #smtp协议默认端口为25
server.set_debuglevel(1) #打印与smtp服务器交互信息
server.login(from_addr, password) #登录
server.sendmail(from_addr, [to_addr], msg.as_string()) #发送邮件
server.quit() #退出服务器




