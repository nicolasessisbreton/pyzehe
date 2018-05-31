"""
6) throw exceptions on invalid user inputs
"""
from sol_2 import *

def is_number(x):
	return isinstance(x, int) or isinstance(x, float)

def is_integer(x):
	return isinstance(x, int)	

def annuity_factor_with_valid(
	table = 'mgdb',
	gender = 'female',
	interest_rate = 0.03,
	age_start = 1,
	annuity_duration = 5,
):

	if table not in mortality_tables:
		raise Exception('table not found: ' + str(table))

	if gender not in ['female', 'male']:
		raise Exception('invalid gender: ' + str(gender))

	if not is_number(interest_rate):
		raise Exception('interest_rate is not a number: ' + str(interest_rate))

	if interest_rate < 0:
		raise Exception('invalid interest_rate: ' + str(interest_rate))

	if not is_integer(age_start):
		raise Exception('age_start is not an integer: ' + str(age_start))
	
	age_min = mortality_tables[table].age_start
	age_max = mortality_tables[table].age_end
	if age_start < age_min or age_start>age_max:
		msg = 'age_start should be in [{:d}, {:d}], received: {:s}'.format(
			age_min,
			age_max,
			str(age_start),
		)
		raise Exception(msg)

	if not is_integer(annuity_duration):
		raise Exception('annuity_duration is not an integer: ' + str(annuity_duration))

	if annuity_duration<0:
		raise Exception('annuity_duration is negative: ' + str(annuity_duration))

	age_final = age_start + annuity_duration
	if age_final>age_max:
		msg = 'final annuity age({:d}) exceed table_age_max ({:d}'.format(
			age_final,
			age_max,
		)
		raise Exception(msg)

	ax = annuity_factor(
		table = table,
		gender = gender,	
		interest_rate = interest_rate,
		age_start = age_start_pre,
		annuity_duration = annuity_duration,
	)

	return ax

# running
# comment every lines below
# except the one that you want to try

# annuity_factor_with_valid(table='wrong_table_name')
# annuity_factor_with_valid(gender='f')
# annuity_factor_with_valid(interest_rate=-1)
# annuity_factor_with_valid(age_start=1000)
annuity_factor_with_valid(annuity_duration=0.5)
