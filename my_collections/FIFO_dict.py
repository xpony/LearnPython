from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self._capacity = capacity   #设置dict容量

	def __setitem__(self, key, value):
		containskey = 1 if key in self else 0
		if len(self) - containskey >= self._capacity: #判断deict是否满了
			last = self.popitem(last=False) #last为真则LIFO,为假则FIFO. popitem()会返回删掉的键值对
			print('remove:', last)
		if containskey:
			del self[key]  #删掉
			print('set:', (key, value))
		else:
			print('add', (key, value))
		OrderedDict.__setitem__(self, key, value)

ld = LastUpdatedOrderedDict(3) #创建一个FIFO的dict
ld['a'] = 1  # add ('a', 1)
ld['b'] = 2  # add ('b', 2)
ld['c'] = 3	 # add ('c', 3)
ld['x'] = 0  #满了，把开头的删掉了
print(ld)    #LastUpdatedOrderedDict([('b', 2), ('c', 3), ('x', 0)])
ld['b'] = 100  #  set: ('b', 100) ,已经存在的，就删掉原来的重新建一个
print(ld)    # LastUpdatedOrderedDict([('c', 3), ('x', 0), ('b', 100)])
