import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from annuity_factor import *
from policy_book import *

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

plt.plot(book.age_start, book.premium)
plt.title('premium by age')
plt.show()

print('pivot table says')
pvt = pd.pivot_table(
	book, 
	values = 'premium',
	index = ['age_start'],
	columns = ['gender', 'annuity_duration'],
	aggfunc = 'count',
)

print(pvt)

book.age_start = book.age_start.round(0)
book.annuity_duration = book.annuity_duration.astype(int)

print('better pivot table says')
pvt_better = pd.pivot_table(
	book, 
	values = 'premium',
	index = ['age_start'],
	columns = ['gender', 'annuity_duration'],
	aggfunc = np.mean,
)

print(pvt_better)

"""
want to know more?
google
	pandas pivot table example
"""