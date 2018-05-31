# arrays as first-class citizens
from numpy import *

# arithmetic
x = array([1, 1, 1])
y = array([2, 2, 2])
print('x+y', x+y)
print('x*y', x*y)
print('x/y', x/y)

# creation
x = ones(3)
print('array of ones', x)

x = zeros(3)
print('array of zeros', x)

x = arange(10)
print('array of increasing', x)

x = linspace(0, 10, 3)
print('array of evenly spaced', x)

# array functions
x = array([1, 2, 3])
print('sum of x', x.sum())
print('mean of x', x.mean())
print('std of x', x.std())
print('min of x', x.min())
print('max of x', x.max())
print('cumulative sum of x', cumsum(x))
print('cumulative product of x', cumprod(x))

y = array([1, 1, 1])
print('maximum(x,y)', maximum(x,y))
print('sum(3*x+y^2-5y)', sum(3*x+y**2-5*y))

# logical operator
x = array([1, 1, 1])
y = array([2, 1, 2])
print('x<y', x<y)
print('all(x<y)', all(x<y))
print('any(x<y)', any(x<y))

# matrix
x = array([[1, 2], [3, 4]])
print('a matrix\n', x)
print('x.sum() and sum(2*x): ', x.sum(), sum(2*x))

y = array([[2, 2], [2, 2]])
print('x*y\n', x*y)

# matrix creation
x = ones((2,2))
y = zeros((2,2))
print('x+y\n', x+y)

z = arange(4).reshape((2,2))
print('z\n', z)

"""
want to know more? 
look at 
	arrays_ops.py
"""
