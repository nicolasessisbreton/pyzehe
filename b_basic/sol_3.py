"""
3) find an annuity factor with a change of table in the middle
   (use the previous function and a new one)
   """
from sol_2 import annuity_factor as ax

def annuity_factor(
	table_pre = 'gam83',
	table_post = 'up94',
	gender = 'female',
	interest_rate = 0.03,
	age_start = 1,
	annuity_duration = 5,
):

	middle = int(annuity_duration/2)

	annuity_duration_pre = middle
	annuity_duration_post = annuity_duration - middle

	age_start_pre = age_start
	age_start_post = age_start + middle

	ax_pre = ax(
		table = table_pre,
		gender = gender,	
		interest_rate = interest_rate,
		age_start = age_start_pre,
		annuity_duration = annuity_duration_pre,
	)

	ax_post = ax(
		table = table_post,
		gender = gender,	
		interest_rate = interest_rate,
		age_start = age_start_post,
		annuity_duration = annuity_duration_post,
	)

	v = (1+interest_rate)**(-annuity_duration_pre)

	r = ax_pre + v*ax_post

	return r

# running
r = annuity_factor(
	table_pre = 'gam83',
	table_post = 'up94',
	gender = 'female',
	interest_rate = 0.03,
	age_start = 30,
	annuity_duration = 20,
)
print('annuity with chg of table in the middle is', r)

