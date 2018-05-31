from numpy import *
import numpy.linalg as linalg

x = array([1, 2, 3])
y = array([
	[1, 2],
	[3, 4],
])

# scalar product
r = x.dot(x)
print('scalar product', r)

# transpose
print('y\n', y)
print('y transpose\n', y.T)

# matrix multiplication
r = y.dot(y)
print('matrix multiplication')
print(r)

# matrix inverse
r = linalg.inv(y)
print('matrix inverse\n', r)

# matrix determinant
r = linalg.det(y)
print('determinant', r)

# solve system of equation and least-square
A = y
b = array([1, 2])
exact = linalg.solve(A, b)
least_square = linalg.lstsq(A,b, rcond=-1)[0]
s = """
solving system exactly, then by least-square
	A x = b
"""
print(s, exact, '\n', least_square)

# covariance
r = cov(x, -2*x)
print('covariance \n', r)

# print correlation
r = corrcoef(x, -2*x)
print('correlation \n', r)


