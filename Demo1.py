class User:
	type = 'USER'

	def __init__(self, name, uid):
		self.name = name
		self.uid = uid

	def __repr__(self):
		return 'im ' + self.name + ' ' + str(self.uid)


class Admin(User):
	type = 'ADMIN'

	def __init__(self, name, uid, group):
		User.__init__(self, name, uid)
		self.group = group

	def __repr__(self):
		return 'im ' + self.name + ' ' + str(self.uid) + ' ' + self.group


class Guest(User):
	def __repr__(self):
		return 'im Guest:' + self.name + ' ' + str(self.uid)


def create_user(type):

	if type == 'USER':
		return User("user1", 1)
	elif type == 'ADMIN':
		return Admin("admin1", 1, "gourp8")
	else:
		return Guest("201", 2)
		#raise ValueError("error")


# 继承与多态：面向对象
if __name__ == '__main__':
	# 继承
	user1 = User("user1", 1)
	print(user1)
	admin1 = Admin("admin1", 1, "gourp8")
	print(admin1)
	# 多态
	print(create_user("uegsd"))