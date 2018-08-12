# coding=utf-8
from collections import UserDict


class StrKeyDict1(UserDict):
	def __missing__(self, key):
		if isinstance(key, str):
			raise KeyError
		return self[str(key)]
	
	def get(self, key, default = None):
		try:
			return self[key]
		except KeyError:
			return default
	
	def __contains__(self, key):
		return str(key) in self.data
	
	def __setitem__(self, key, item):
		self.data[str(key)] = item


if __name__ == '__main__':
	d = StrKeyDict1([('2', 'two'), ('4', 'four')])
	d[5] = 'five'
	print(d['5'])
	print(d['2'])
	print(d[4])
	# # print(d[1])
	# print(d.get('2'))
	# print(d.get(4))
	# print(d.get('5'))
	print(2 in d)
	print(1 in d)
