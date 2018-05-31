"""
4) use a class to bundle all the previous functionality
	(set all parameters with __init__)
	(precompute any possible quantity)
	(compute the annuity from the precomputed values)

"""
from mortality import *

class Annuity:
	def __init__(
		self,
		table = 'test',
		gender = 'female',
		interest_rate = 0.03,
	):
		self.table = mortality_tables[table]
		qx = mortality_tables[table][gender]
		self.px = [1-x for x in qx]
		self.v = 1/(1+interest_rate)

	def value(
		self,
		age_start = 1,
		annuity_duration = 5,
	):
		n = annuity_duration+1
		vk = [1]*n
		kpx = [1]*n

		age_start_qx = self.table.age_start
		offset = age_start - age_start_qx

		for i in range(1, n):
			vk[i] = self.v**i
			kpx[i] = kpx[i-1]*self.px[offset+i-1]

		ax = 0
		for i in range(n):
			ax += vk[i]*kpx[i]

		return ax

# running
ax = Annuity()
r = ax.value()
print('annuity class says', r)