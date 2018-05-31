def f(x,y,z):
	return x+y+z

r = f(1,2,3)
print('standard call says', r)

r = f(x=1, y=2, z=3)
print('named call says', r)

def f_with_default(x=1, y=2, z=3):
	return f(x,y,z)

r = f()
print('f with default says')