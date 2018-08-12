
# coding=utf-8

def make_averager():
	count = 0
	total = 0
	print('d')
	
	def averager(new_value):
		#IMMUTABLE NEED NON LOCAL DECLARATIONS ->NUMBERS, TUPLES, STRING
		nonlocal count, total
		count +=1
		total +=new_value
		return total/count
	
	return averager

if __name__ == '__main__':
    avg = make_averager()
    print(avg)
    print(avg(10))
    print(avg(11))
    
