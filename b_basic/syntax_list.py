# creating a list
x = [1, 3]
print('creation', x)

# adding element
x.append(4)
x += [5]
x.insert(1, 2) # insert(position, element)
print('adding element', x)

# picking element
print('picking', x[0], x[1])
print('picking a lot', x[:3], x[1:], x[2:5], x[-3:-1])

# copying over all element from another list
x = [1, 2]
y = [3, 4]
x.extend(y)
z = [1,2]
z.append(y)
print('copying over for x', x)
print('copying over for z', z)

# iterating through all element
x = [1, 2, 3, 4]
for i in x:
	print('iteration says', i)

# list comprehension
x = [1, 2, 3]
y = [i+1 for i in x]
print('list comprehension says', y)

# modifying element
x = [1, 2, 3]
for i in range(len(x)):
	x[i] *= 2
print('modifying says', x)
