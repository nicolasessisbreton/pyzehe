from numpy.testing import *
from annuity_package import *

r = annuity_factor(
	table = 'mgdb',
	gender = 'female',
	interest_rate = 0.03,
	age_start = 50,
	annuity_duration = 20,
)
assert_almost_equal(r, 15.279116, 4)

print('all tests passed')

