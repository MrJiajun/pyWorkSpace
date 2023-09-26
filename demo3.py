#-*-encoding=UTF-8

def log(level, *args, **kvargs):
	def inner(func):
		def wrapper(*args, **kvargs):
			'''
			*用来传递任意个无名字参数，这些参数会一个Tuple的形式访问。**用来处理传递任意个有名字的参数，这些参数用dict来访问
			'''
			print(level, 'before calling ', func.__name__)
			print(level, 'args:', args, 'kvargs:', kvargs)
			func(*args, **kvargs)
			print(level, 'after calling ', func.__name__)
		return wrapper
	return inner


@log(level='INFO')
def kingdee(name, msg):
	print('kingdee', name, msg)


#装饰器
if __name__ == '__main__':
	kingdee(name='eas', msg='fin is best')