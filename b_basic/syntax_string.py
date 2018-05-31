s = 'a string {:s} format and {:d} number: {:f}'
f = s.format(
	'with',
	1,
	3.14,
)

print(f)

s = """ 
various format
	string {:s}
	integer {:d}
	float {:f}
	float with #decimal {:.2f}
"""
print(s.format(
	'hello', 1, 1/3, 1/3
))

s = """ 
named format
	string {a:s}
	integer {b:d}
	float {c:f}
	float with #decimal {d:.2f}
"""
print(s.format(
	a = 'hello', 
	b = 1, 
	c = 1/3, 
	d = 1/3
))

