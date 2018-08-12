
# coding=utf-8
import time
import functools


def clocked(func):
	def clocked(*args):
		t0 =time.perf_counter()
		result = func(*args)
		elapsed = time.perf_counter() - t0
		name = func.__name__
		
		arg_str = ', '.join(repr(arg) for arg in args)
		print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
		return result
	return clocked

@clocked
def snooze(seconds):
	time.sleep(seconds)
	
@functools.lru_cache()
@clocked
def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    # print('*'*40,'Calling snooze(.123)')
    # snooze(1.0)
    
    fibonacci(3)



		