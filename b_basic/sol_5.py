"""
5) add the choice between a nominal and an effective interest rate
"""
from mortality import *

class Annuity:
	def __init__(
		self,
		table = 'test',
		gender = 'female',
		interest_rate = 0.03,
		interest_compounding = 12,
	):
		self.table = mortality_tables[table]
		qx = mortality_tables[table][gender]
		self.px = [1-x for x in qx]

		v = (1+interest_rate/interest_compounding)**(1/interest_compounding)
		self.v = 1/v

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
print('annuity with compounded interest says', r)