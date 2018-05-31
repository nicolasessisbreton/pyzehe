"""
Refactor:

1) annuity_factor such that:
		conversion to integer is handled,
		no extra printing
"""
from numpy import *
from mortality import *

def annuity_factor(
	table = 'mgdb',
	gender = 'female',
	interest_rate = 0.03,
	age_start = 50,
	annuity_duration = 20,
):
	qx = mortality_tables[table][gender]
	qx = array(qx)
	px = 1 - qx

	n = annuity_duration+1
	n = int(n)

	v = 1/(1+interest_rate)
	vk = v**arange(n)

	age_start_qx = mortality_tables[table].age_start
	offset = age_start - age_start_qx
	offset = int(offset)
	kpx = px[offset:offset+n]
	kpx[0] = 1
	kpx = kpx.cumprod()

	ax = sum(vk*kpx)

	return ax

# running
ax_1 = annuity_factor(age_start=30, annuity_duration=10)
ax_2 = annuity_factor(age_start=30.75, annuity_duration=10.5)
print('annuities are', ax_1, ax_2)
