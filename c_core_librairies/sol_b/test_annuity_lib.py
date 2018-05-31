from numpy.testing import *
from annuity_lib import *

r = annuity_factor(
	table = 'mgdb',
	gender = 'female',
	interest_rate = 0.03,
	age_start = 50,
	annuity_duration = 20,
)
assert_almost_equal(r, 15.279116, 4)

b = Book(10)

assert_almost_equal(b.premium.sum(), 137.7770, 4)

print('all tests passed')

