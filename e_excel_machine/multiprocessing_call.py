from numpy import *
from numpy.random import *
from multiprocessing import Pool, cpu_count
from itertools import starmap
import pathlib
from config import *

def get_value(interest_rates, strikes, sigmas, S_0s):
	path = pathlib.Path(__file__).resolve().parents[0]
	path = str(path) + r'\binomial_model.xlsx'
	w = ap.Workbook(path)
	s = w.Worksheets['crr']

	interest_rate = s.Cells['B1']
	strike = s.Cells['B2']
	sigma = s.Cells['B3']
	S_0 = s.Cells['B4']
	price = s.Cells['B5']

	r = []
	for ndx in range(len(interest_rates)):
		i = interest_rates[ndx]
		k = strikes[ndx]
		s = sigmas[ndx]
		s0 = S_0s[ndx]

		interest_rate.PutValue.Overloads[float](i)
		strike.PutValue.Overloads[float](k)
		sigma.PutValue.Overloads[float](s)
		S_0.PutValue.Overloads[float](s0)

		w.CalculateFormula()

		# print(i, k, s, s0, price.StringValue) # debug
		# w.Save('out.xlsx') # debug

		p = price.DoubleValue

		r += [p]

	return r

def parallel_eval(interest_rates, strikes, sigmas, S_0s):
	nb_chunk = cpu_count()
	nb_chunk = min(nb_chunk, 5) # maximum of 10 concurrent workbook on aspose trial license

	n = len(interest_rates)
	chunk = array_split(arange(n), nb_chunk)
	args = (
		(
			interest_rates[ndx],
			strikes[ndx],
			sigmas[ndx],
			S_0s[ndx],
		)
		for ndx in chunk
	)
	pool = Pool(nb_chunk)
	prices = pool.starmap(get_value, args) # for release
	# prices = starmap(get_value, args) # for debug
	prices = [item for sublist in prices for item in sublist]
	pool.close()

	return prices

# work
if __name__ == '__main__':
	interest_rates = uniform(0.01, 0.1, 10)
	strikes = uniform(30, 50, 10)
	sigmas = uniform(0.1, 0.3, 10)
	S_0s = uniform(30, 50, 10)

	prices = parallel_eval(interest_rates, strikes, sigmas, S_0s)

	for ndx in range(len(interest_rates)):
		s = 'i{:.2f} K{:.2f} s{:.2f} s0{:.2f} p{:.2f}'.format(
			interest_rates[ndx],
			strikes[ndx],
			sigmas[ndx],
			S_0s[ndx],
			prices[ndx],
		)
		print(s)



