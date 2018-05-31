d = dict(
	a = 1,
	b = 2,
)

print('iterating through the keys')
for key in d.keys():
	print(key)

print('iterating through the values')	
for value in d.values():
	print(value)

print('iterating through the keys and values')
for key, val in d.items():
	print(key, val)
