
# coding=utf-8

import itertools
class ArithmeticProgression:
	def __init__(self, begin, step, end=None):
		self.begin = begin
		self.step = step
		self.end = end
	
	def __iter__(self):
		result = type(self.begin + self.step)(self.begin)
		forever= self.end is None
		index = 0
		while forever or result <self.end:
			yield result
			index +=1
			result = self.begin +self.step*index
			
def aritprog_gen(begin, step, end=None):
	first = type(begin + step)(begin)
	ap_gen = itertools.count(first, step)
	if end is not None:
		ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
	return ap_gen

if __name__ == '__main__':
    art_pro = ArithmeticProgression(1,0.5,3)
    print(art_pro)
    for i in art_pro:
	    print(i)