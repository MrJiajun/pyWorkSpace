#-*-encoding=UTF-8
def log(func):
	def wrapper():
		print('before calling ', func.__name__)
		func()
		print('after calling ', func.__name__)
	return wrapper



#注解
@log
def kingdee():
	print('kingdee')


#装饰器
if __name__ == '__main__':
	kingdee() #= log(kingee())