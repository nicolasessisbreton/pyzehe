from config import *

print('# address')
print(address.head(10), '\n')

print('# describe says')
print(address.describe(include='all'), '\n')

print('# dtypes')
print(address.dtypes, '\n')

print('# sorted address')
sorted_address = address.sort_values(['cid', 'date'])
print(sorted_address.head(10), '\n')

print('# are address in sorted order')
x = address.reset_index()
y = sorted_address.reset_index()
z = pd.concat([x,y], axis=1)
print(z.head(10), '\n')

print("# what's the relation between client and address")
x = client.merge(address, on='cid', how='left', suffixes=('', '_'))
x = x[['cid', 'date', 'city', 'city_', 'phone', 'phone_']]
print(x.head(20), '\n')
