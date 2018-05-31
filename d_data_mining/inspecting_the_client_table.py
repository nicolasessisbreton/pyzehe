import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.expand_frame_repr', False)

db_path = 'db.sqlite3'
db = sqlite3.connect(db_path)

client = pd.read_sql('select * from client', db)

print('# describe says')
print(client.describe(include='all'), '\n')

print('# dtypes')
print(client.dtypes, '\n')

client.date_of_birth = pd.to_datetime(client.date_of_birth)
print('# date_of_birth after conversion:', client.date_of_birth.dtypes, '\n')

print('# age 1')
client['age'] = pd.to_datetime('2018-01-01') - client.date_of_birth
print(client.age.describe(), '\n')

print('# age 2')
client.age = client.age.dt.days/365.25
print(client.age.describe(), '\n')

plt.title('age hist')
client.age.hist()
plt.show()

print('# client with age\n', client.head(10), '\n')