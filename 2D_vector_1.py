
# coding=utf-8

import math
from array import array

class Vector2d:
	typecode ='d'
	
	def __init__(self, x,y):
		self.__x = float(x)
		self.__y = float(y)
		
	@property
	def x(self):
		return  self.__x
	
	@property
	def y(self):
		return self.__y
	
	def __repr__(self):
		class_name = type(self).__name__
		return '{}({!r}, {!r})'.format(class_name, *self)
	
	def __str__(self):
		return str(tuple(self))
	
	def __bytes__(self):
		return (bytes([ord(self.typecode)]) +
				bytes(array(self.typecode,self)))
	
	def __hash__(self):
		return hash(self.x) ^ hash(self.y)
	
	def __format__(self, fmt_spec=''):
		if fmt_spec.endswith('p'):
			fmt_spec = fmt_spec[:-1]
			coords = (abs(self),self.angle())
			outer_fmt = '<{}, {}>'
		else:
			coords = self
			outer_fmt = '({}, {})'
		
		components = (format(c,fmt_spec) for c in coords)
		return '({},{})'.format(*components)
	
	def __abs__(self):
		return math.hypot(self.x, self.y)
	
	def __iter__(self):
		return (i for i in (self.x,self.y))
	
	def __bool__(self):
		return bool(abs(self))
	
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector2d(x, y)
	
	def __mul__(self, scalar):
		return Vector2d(self.x * scalar, self.y * scalar)
	
	def __getitem__(self, item):
		if isinstance(item,str):
			return self.x if item == 'x' else self.y
		else:
			return self.x if item == 0 else self.y
	
	def __eq__(self, other):
		return tuple(self) == tuple(other)
	
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector2d(x,y)
	
	def angle(self):
		return math.atan2(self.y, self.x)
if __name__ == '__main__':
	v1 = Vector2d(3,4)
	v2 = Vector2d(4,5)
	
	v3 = v1+v2
	
	# print(v1)
	# v2 = eval(repr(v1))
	# print(v2)
	#
	# v3= bytes(v1)
	# print(v3)
	#
	# v4 = format(v1,'p')
	# print(v4)
	# v4 = format(v1,'.1p')
	# print(v4)
	#
	# print(set([v1]))
	# v5 = hash(v1)
	# print(v5)