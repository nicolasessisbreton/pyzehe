"""
1) find the client with the highest aggregate amount of purchase
"""
from config import *

x = fund_price.groupby('fund')['price'].mean()
x = x.to_frame()
x = x.sort_values('price', ascending=False)
printn(x, 'sorted mean price')

x = x.reset_index()
third_highest = x.iloc[2,0]
print('3rd highest: ' + third_highest)

x = fund_price.query('fund == @third_highest')
printn(x, '3rd highest prices')

x = x.sort_values('price')
x = x['price']
x = x.rolling(2).mean()
printn(x, 'rolling mean')
