"""
1) find and annuity factor from the minimum age to the maximum age
"""
from mortality import *

qx = mortality_tables.test.female
px = [1-x for x in qx]

v = 1/1.03
n = len(px)+1
vk = [1]*n
kpx = [1]*n
for i in range(1, n):
	vk[i] = v**i
	kpx[i] = kpx[i-1]*px[i-1]

ax = 0
for i in range(n):
	ax += vk[i]*kpx[i]

print('annuity is', ax)
