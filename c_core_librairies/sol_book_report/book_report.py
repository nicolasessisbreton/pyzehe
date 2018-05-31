import sys
import xlwings as xw

import pathlib
path = pathlib.Path(__file__).resolve().parents[1]
path = str(path)
sys.path.append(path)
import book_premium as bp
import matplotlib.pyplot as plt

@xw.func
@xw.ret(expand='table')
def show():
    return bp.pvt_better

@xw.func
def annuity_factor(
	table = 'mgdb',
	gender = 'female',
	interest_rate = 0.03,
	age_start = 50,
	annuity_duration = 20,
):
	return bp.annuity_factor(
		table, 
		gender, 
		interest_rate, 
		int(age_start), 
		int(annuity_duration),
	)

@xw.func
def plot_premium_hist(nbin):
	nbin = int(nbin)
	sht = xw.Book.caller().sheets.active
	fig = plt.figure()
	plt.hist(bp.book.premium, bins=nbin)
	sht.pictures.add(fig, name='premium_hist', update=True)
	return 'premium hist with {:d} bins'.format(nbin)

"""
want to know more?
google 
	xlwings udf
	xlwings array formula
	xlwings matplotlib
"""