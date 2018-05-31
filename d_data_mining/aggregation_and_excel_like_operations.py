from config import *

printn(guarantee_cost, 'guarantee_cost')

printn('average guarantee')
x = guarantee_cost.groupby('guarantee')['fee'].mean()
printn(x)

printn('guarantees stat')
stat = guarantee_cost.groupby('guarantee')['fee'].aggregate(dict(
	fee = [
		'min', 'max', 'mean', 'std', 'size',
		lambda x: np.percentile(x,.9),
	],
))
printn(stat)

printn('stats on many columns')
x = guarantee_cost.copy(1)
x['fee2'] = x.fee*2
r = x.groupby('guarantee')['fee', 'fee2'].agg(['mean', 'std'])
printn(r)

printn('different stats per column')
r = x.groupby('guarantee')['fee', 'fee2'].agg(dict(
	fee = ['mean', 'std'],
	fee2 = ['min', 'max'],
))
printn(r)

printn('melting a table')
r = r.reset_index()
printn(pd.melt(r, id_vars=['guarantee'])) 

printn('cumulative cost over time')
g = guarantee_cost.sort_values(['guarantee', 'date'])
cost = []
guarantee = None
last_cost = 1
r = 0
for row in g.itertuples(index=False):
	if row.guarantee == guarantee:
		t = row.date - last_date
		t = t.days/365.25
		r = last_cost * last_fee**t
	else:
		guarantee = row.guarantee
		last_fee = 1+row.fee
		last_date = row.date
		last_cost = 1
		r = last_cost

	cost += [r]

g['cost'] = cost
printn(g)

