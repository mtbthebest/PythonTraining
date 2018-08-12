
# coding=utf-8

class Demo:
	@classmethod      # first arguments ->class
	def klassmeth(*args):
		return args
	
	@staticmethod      # arguments ->function parameters .similar to Normal function
	def statmeth(*args):
		return args

if __name__ == '__main__':
    print(Demo.klassmeth())
    print(Demo.klassmeth('spam'))
    print(Demo.statmeth())
    print(Demo.statmeth('spam'))


