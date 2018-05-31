"""
1) In multiprocessing_call.py, 7 lines needs refactoring.
	 Find them and help them.

2) Rewrite multiprocessing_call.py such that get_value uses a dataframe

3) In embedding_the_machine_in_excel.py:
	- create a get_value excel function that returns the price for
		an individual set of parameters
		(ex: get_value(0.06, 40, 0.25, 36) 

	- compare the speed in excel of get_value vs the parallel_eval function
	(from a big table of parameters, compute the prices with:)
	(several excel cells with get_value)
	(vs one matrix cell with parallel_eval)
"""