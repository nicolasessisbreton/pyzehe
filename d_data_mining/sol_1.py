"""
1) find the client with the highest aggregate amount of purchase
"""
from config import *

x = purchase.groupby(['cid'])['amount'].sum()
x = x.reset_index()
x = x.rename(columns=dict(amount='total_purchase'))
printn(x, 'grouped')

max_purchase = x.total_purchase.max()
printn(max_purchase, 'max purchase')

mask = x.total_purchase == max_purchase
x = x[mask]
printn(x, 'wanted client')

# this is slow
d = client.query('cid in @x.cid')
printn(d, 'wanted client info (slow)')

# this is fast
d = client.merge(x, on='cid')
printn(d, 'wanted client info (fast)')
