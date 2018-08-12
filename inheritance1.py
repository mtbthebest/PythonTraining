
# coding=utf-8
from collections import UserDict

class DoppeDict1(dict):
	def __setitem__(self, key, value):
		super().__setitem__(key,[value] *2)

class DoppeDict2(UserDict):
	def __setitem__(self, key, value):
		super().__setitem__(key,[value] *2)
		

class Base:
	def __init__(self,**kwds):
		print('Base')
		self.base = kwds
	
	def func(self):
		return 'base function'

class Derived(Base):
	def __init__(self,**kwds):
		print('Derived')
		super().__init__(**kwds)
		print(self.base)
		func = self.func()
		print(func)
		





if __name__ == '__main__':
    # dd = DoppeDict1(one=1)
    # print(dd)
    # dd['two']= 3
    # dd.update(three=4)
    # print(dd)
	#
    # dd = DoppeDict2(one = 1)
    # print(dd)
    # dd['two'] = 3
    # dd.update(three = 4)
    # print(dd)
    
    d = Derived(base =4)
    