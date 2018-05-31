import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

client.date_of_birth = pd.to_datetime(client.date_of_birth)
address.date = pd.to_datetime(address.date)
purchase.date = pd.to_datetime(purchase.date)
guarantee_cost.date = pd.to_datetime(guarantee_cost.date)
fund_price.date = pd.to_datetime(fund_price.date)

client['age'] = pd.to_datetime('2018-01-01') - client.date_of_birth
client.age = client.age.dt.days/365.25

def printn(df, head=20, title=None):
	if isinstance(head, str):
		title = head
		head = 20

	head = int(head)

	if isinstance(df, pd.DataFrame):		
		x = df.head(head)
	elif isinstance(df, str):
		title = df
		x = None
	else:
		x = df
		
	if title:
		print('# ' + title)
	if x is not None:
		print(x, '\n')
