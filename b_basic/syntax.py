# this is a comment

"""
this is a multiline comment
"""

# variables
a_string_variable = 'fish and chips'

a_multiline_string = """
	I'm on
	on several lines
"""

a_number = 2.5

a_list = [1, 'two', 3]

a_dictionary = dict(
	cat = 'meow',
	dog = 'ouf',
)

another_dict = {
	'strange key': 1,
	'better_key': 2,
}

# list
x = [1, 2, 3]
print('list says', x)
print('list 1 is', x[1])

# dict
x = dict(a=1, b=2)
print('dict says', x)
print('dict a is', x['a'])

# if else
x = 1
if x>0:
	print('x is gt 0')
elif x<0:
	print('x is lt 0')
else:
	print('x is eq 0')

# for loop
for i in range(3):
	print('for loop says', i)

# function
def add(x, y):
	r = x + y
	return r

z = add(1,2)

print('fct says', z)

# class
class Actuary:
	def add(self, x, y):
		r = x*y
		return r

a = Actuary()
z = a.add(1,2)
print('actuary says', z)

# import
import hello_world
import hello_world as hw

from utils import *
x = DataDict(a=1, b=2)
print('a better dict says a is', x.a)

"""
want to know more? 
look at 
	syntax_*.py
		( type ctrl+p syntax_
"""