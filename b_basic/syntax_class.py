class A:
	def __init__(self, x):
		self.x = x

	def add(self, y):
		return self.x + y


a = A(1)
print('class x says', a.x)

r = a.add(1)
print('class add says', r)