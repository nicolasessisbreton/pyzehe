import sys
import xlwings as xw
import numpy as np
import pandas as pd
import pathlib
path = pathlib.Path(__file__).resolve().parents[1]
path = str(path)
sys.path.append(path)
import multiprocessing_call as mc

@xw.func
@xw.arg('x', np.array, ndim=2)
@xw.ret(expand='table')
def parallel_eval(x):
	print('parallel_eval', x.shape)
	r = mc.parallel_eval(
		interest_rates = x[:,0],
		strikes = x[:,1], 
		sigmas = x[:,2], 
		S_0s = x[:,3],
	)
	r = np.array(r)[:,None]
	return r

"""
the code below is for debug

in cmder
	python embedding_the_machine_in_excel.py

then open the associated workbook

in the workbook make sure the xlwings options are
	debug udf 1
	udf use server 1

then
	any print message will be displayed in the terminal
"""
if __name__ == '__main__':
	xw.serve()