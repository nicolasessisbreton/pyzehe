# here is a book of randomly generated policies
from numpy import *
from numpy.random import *
import pandas as pd

set_printoptions(linewidth=1e99)

nb_contract = 10

seed(0)

age_start = uniform(20, 60, nb_contract)

gender = choice(['female', 'male'], nb_contract)

annuity_duration = normal(15, 20, nb_contract)
annuity_duration = minimum(maximum(annuity_duration, 1), 40)

print('age_start', age_start)
print('gender', gender)
print('annuity_duration', annuity_duration)

book = pd.DataFrame(dict(
	age_start = age_start,
	gender = gender,
	annuity_duration = annuity_duration,
))

print('book')
print(book)

"""
want to know more?
google
	numpy random lognormal	
	numpy random binomial

	pandas dataframe example
"""