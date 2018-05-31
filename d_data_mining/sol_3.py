"""
3) plot the evolution of the guarantee fees over time
"""
from config import *

x = guarantee_cost
printn(x, 'guarantee fees')

x = pd.pivot_table(
	x, 
	values = 'fee',
	index = ['date'],
	columns = ['guarantee'],
	aggfunc = np.mean,
)

printn(x, 'pivoted')

x = x.reset_index()
x.plot(x='date', y=['gmdb', 'gmwb'])
plt.show()