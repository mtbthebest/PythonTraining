
# coding=utf-8

from functools import reduce
from operator import add

def factorial(n):
	""":return n!"""
	return 1 if n<2 else n * factorial(n-1)





if __name__ == '__main__':
	print(factorial(10))
	print(factorial.__doc__)
	
	b = map(factorial,range(10))
	print(list(b))
	
	c = list(map(factorial, filter(lambda n: n%2, range(6))))
	print(c)
	
	d=reduce(add,range(5))
	print(d)
	
