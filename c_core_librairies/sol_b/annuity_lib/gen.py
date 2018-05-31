from numpy import *
from numpy.random import *
import matplotlib.pyplot as plt
import pandas as pd
from .factor import *

set_printoptions(linewidth=1e99)
seed(0)

class Book:
	def __init__(self, nb_contract=10):
		# making
		nb_contract = int(nb_contract)
		age_start = uniform(20, 60, nb_contract)

		gender = choice(['female', 'male'], nb_contract)

		annuity_duration = normal(15, 20, nb_contract)
		annuity_duration = minimum(maximum(annuity_duration, 1), 40)


		book = pd.DataFrame(dict(
			age_start = age_start,
			gender = gender,
			annuity_duration = annuity_duration,
		))

		# premium
		premium = zeros(nb_contract)

		for i in range(nb_contract):
			premium[i] = annuity_factor(
				table = 'mgdb',
				gender = book.gender[i],
				interest_rate = 0.03,
				age_start = int(age_start[i]),
				annuity_duration = int(annuity_duration[i]),
			)

		book['premium'] = premium

		# saving
		self.nb_contract = nb_contract
		self.age_start = age_start
		self.gender = gender
		self.annuity_duration = annuity_duration
		self.book = book
		self.premium = premium

	def view_policies(self):
		print('nb_contract', self.nb_contract)
		print('age_start', self.age_start)
		print('gender', self.gender)
		print('annuity_duration', self.annuity_duration)
		print('premium', self.premium)
		print('book')
		print(self.book)

	def view_stats(self):
		self.book.age_start.hist()
		plt.title('age_start hist')
		plt.show()

	def get_pivot_table(self):	
		book = self.book.copy(1) # make a copy as the pivot table modifies the book

		book.age_start = book.age_start.round(0)
		book.annuity_duration = book.annuity_duration.astype(int)

		pvt = pd.pivot_table(
			book, 
			values = 'premium',
			index = ['age_start'],
			columns = ['gender', 'annuity_duration'],
			aggfunc = mean,
		)

		return pvt

