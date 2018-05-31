"""
2) use a function to make every parameter flexible
	 (age, duration, mortality table, interest rate)
 """
from mortality import *

def annuity_factor(
	table = 'test',
	gender = 'female',
	interest_rate = 0.03,
	age_start = 1,
	annuity_duration = 5,
):
	qx = mortality_tables[table][gender]
	px = [1-x for x in qx]

	v = 1/(1+interest_rate)
	n = annuity_duration+1
	vk = [1]*n
	kpx = [1]*n

	age_start_qx = mortality_tables[table].age_start
	offset = age_start - age_start_qx

	for i in range(1, n):
		vk[i] = v**i
		kpx[i] = kpx[i-1]*px[offset+i-1]

	ax = 0
	for i in range(n):
		ax += vk[i]*kpx[i]

	return ax

# running
r = annuity_factor(
	table = 'test',
	gender = 'female',
	interest_rate = 0.03,
	age_start = 1,
	annuity_duration = 5,
)
print('annuity is', r)

r = annuity_factor(table='gam83', age_start=20)
print('annuity is', r)
