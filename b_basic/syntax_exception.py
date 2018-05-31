# catching an exception
try:
	x = 1/0
except Exception as e:
	print('the following exception was raise:', e)

# custom exception
class IsBiggerThan5(Exception):
	pass

class IsLessThan0(Exception):
	pass

def f(x):
	if x<0:
		raise IsLessThan0()
	elif x>5:
		raise IsBiggerThan5()
	else:
		raise Exception()

def catcher(x):
	try:
		f(x)
	except IsBiggerThan5:
		print('bigger>5 thrown')
	except IsLessThan0:
		print('less<0 thrown')
	except:
		print('something thrown')

catcher(10)
catcher(-10)
catcher(0)

# raising an exception
# you will get an exception
raise Exception('keep calm, and run the code again')