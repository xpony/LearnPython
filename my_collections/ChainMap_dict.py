import argparse, os
from collections import ChainMap

# 构造缺省参数(默认参数)
defaults = {
	'color' : 'red',
	'user' : 'guest'
}

# 构造命令行参数
p = argparse.ArgumentParser() #创建一个解析器
p.add_argument('-u', '--user') #添加参数 意思：-u时 跟user
p.add_argument('-c', '--color')
namespace = p.parse_args() #把参数解析到namespance
command_line_args = {k:v for k, v in vars(namespace).items() if v} #按条件生成一个dict

#组合成ChainMap
combined = ChainMap(command_line_args, os.environ, defaults) #查找顺序从左至右

#打印参数
print('color: %s' % combined['color']) #给key,它会依次在自己的子dict中查找
print('user: %s' % combined['user'])