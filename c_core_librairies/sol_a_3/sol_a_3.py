"""
Refactor:
3) book_report such that: 
		it uses all the previous improvements
"""
import sys
import xlwings as xw

import pathlib
path = pathlib.Path(__file__).resolve().parents[1]
path = str(path)
sys.path.append(path)
from sol_a_2 import Book

@xw.func
@xw.ret(expand='table')
def show(nb_contract):
	b = Book(nb_contract)
	return b.get_pivot_table()

