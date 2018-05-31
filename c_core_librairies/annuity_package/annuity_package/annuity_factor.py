from numpy import *
from .mortality import *

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

	v = 1/(1+interest_rate)
	vk = v**arange(n)

	age_start_qx = mortality_tables[table].age_start
	offset = age_start - age_start_qx
	kpx = px[offset:offset+n]
	kpx[0] = 1
	kpx = kpx.cumprod()

	ax = sum(vk*kpx)

	return ax

