import xlwings as xw
from annuity_lib import *

@xw.func
@xw.ret(expand='table')
def show(nb_contract):
	b = Book(nb_contract)
	return b.get_pivot_table()

