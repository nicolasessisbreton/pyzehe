import sqlite3
import pandas as pd

pd.set_option('display.expand_frame_repr', False)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

db_path = 'db.sqlite3'
db = sqlite3.connect(db_path)

client = pd.read_sql('select * from client', db)
address = pd.read_sql('select * from address', db)
purchase = pd.read_sql('select * from purchase', db)
guarantee_cost = pd.read_sql('select * from guarantee_cost', db)
fund_price = pd.read_sql('select * from fund_price', db)

print('# client\n', client.head(10), '\n')
print('# address\n', address.head(10), '\n')
print('# purchase\n', purchase.head(10), '\n')
print('# guarantee_cost\n', guarantee_cost.head(10), '\n')
print('# fund_price\n', fund_price.head(10), '\n')

"""
live
	make head(10) into a parameter: head(nb_head)
	circulate in result with: '#'
"""