
# coding=utf-8

from math import hypot


class Vector:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return 'Vector(%r,%r)' % (self.x, self.y)
	
	def __abs__(self):
		return hypot(self.x, self.y)
	
	def __bool__(self):
		return bool(abs(self))
	
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)
	
	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)
	
	def __getitem__(self, item):
		if isinstance(item,str):
			return self.x if item == 'x' else self.y
		else:
			return self.x if item == 0 else self.y
	
if __name__ == '__main__':
	v1 = Vector(2, 4)
	v2 = Vector(2, 1)
	v3 = v1 + v2
	print(v3)
	v4 = abs(v1)
	print(v4)
	v5 = bool(v2)
	print(v5)
	v6 = Vector(4,0)
	print(v6['x'])
	print(v6[0])
