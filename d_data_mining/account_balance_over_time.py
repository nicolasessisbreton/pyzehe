from config import *

printn(purchase, 10, 'purchase')
printn(fund_price, 'fund_price')

printn('account balance for client 5')
purchase_of_5 = purchase.query('cid==5')
printn(purchase_of_5, 'client 5 purchase')

fund_of_5 = purchase_of_5.fund.unique()
printn(fund_of_5, 'funds purchased by client 5')

printn('fund_price for client 5 purchase')
fund_price_of_5 = fund_price.query("fund in @fund_of_5")
printn(fund_price_of_5)

printn('fund_price_of_5 sorted')
fund_price_of_5 = fund_price_of_5.sort_values(['fund', 'date'])
printn(fund_price_of_5)

printn('price of each purchased')
purchase_of_5 = purchase_of_5.sort_values('date')
fund_price_of_5.sort_values('date', inplace=True)
purchase_of_5 = pd.merge_asof(purchase_of_5, fund_price_of_5, on='date', by='fund')
printn(purchase_of_5)

printn('account balance over time')
def f(row):
	x = purchase_of_5.query('date<=@row.date').copy(1)
	x.date = row.date
	x = pd.merge_asof(x, fund_price_of_5, on='date', by='fund')

	x['value'] = x.price_y/x.price_x * x.amount

	r = pd.Series(dict(
		value = x.value.sum()
	))

	r = pd.concat([row, r])

	return r

purchase_of_5 = purchase_of_5.apply(f, axis=1)
printn(purchase_of_5)

printn('viewing an intermediate step of the above')
row = purchase_of_5.query('fund=="rowe"').T.squeeze()
x = purchase_of_5.query('date<=@row.date').copy(1)	
x.date = row.date
x = pd.merge_asof(x, fund_price_of_5, on='date', by='fund')
x['value'] = x.price_y/x.price_x * x.amount
printn(x)