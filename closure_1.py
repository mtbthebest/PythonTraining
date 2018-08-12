
# coding=utf-8

def make_averager():
	series = []
	print('d')
	
	def averager(new_value):
		series.append(new_value)
		total = sum(series)
		return total/len(series)
	
	return averager

if __name__ == '__main__':
    avg = make_averager()
    print(avg)
    print(avg(10))
    print(avg(11))
    
