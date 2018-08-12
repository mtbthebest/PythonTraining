# coding=utf-8

import math
from array import array
import reprlib
import numbers
import functools
import operator
import itertools


class yrange:
	def __init__(self, n):
		self.i = 0
		self.n = n
	
	def __iter__(self):
		print('self : ',self)
		return self
	
	def __next__(self):
		print('next')
		if self.i < self.n:
			i = self.i
			self.i += 1
			return i
	
		else:
			raise StopIteration()
		


if __name__ == '__main__':
	y = yrange(3)
	# print(y)
	# print(y.__next__())
	# print(y.__next__())
	# print(y.__next__())
	# print('Starting to iter')
	for elem in y:
		print(elem)
