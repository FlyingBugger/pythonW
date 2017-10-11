import sys
def test():
	args=sys.argv
	if len(args)==1:
		print('hello')
	elif len(args)==2:
		print('hello,%s'%args[1])

if __name__=='__main__':
	test()


