"""
# annuity factor

Use the mortality table in 'mortality.py' to:

1) find an annuity factor from the minimum age to the maximum age

2) use a function to make every parameter flexible
	 (age, duration, mortality table, interest rate)

3) find an annuity factor with a change of table in the middle
   (use the previous function and a new one)

4) use a class to bundle all the previous functionality
	(set all parameters with __init__)
	(precompute any possible quantity)
	(compute the annuity from the precomputed values)

5) add the choice between a nominal and an effective interest rate

6) throw exceptions on invalid user inputs

# recall 

The formula for an annuity is

	ax = sum_{k=0}^{omega-x} vk kpx

"""