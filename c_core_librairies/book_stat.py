import matplotlib.pyplot as plt
from policy_book import book

plt.plot(book.age_start)
plt.title('age_start')
plt.show()

plt.hist(book.age_start)
plt.title('age_start hist')
plt.show()

book.age_start.hist()
plt.title('pandas age_start hist')
plt.show()

print('pandas describe says')
d = book.age_start.describe()
print(d)

"""
want to know more?
google
	matplotlib legend example
	matplotlib scatter plot example
	matplotlib 3d plot example
	matplotlib histogram example
"""