from numpy import *
from numpy.random import *
import pandas as pd
import sqlite3
from os import remove
from os.path import exists
from itertools import combinations

db_path = 'db.sqlite3'
force = 1

nb_client = 1e1
nb_guarantee = 1e1
nb_fund_price = 1e1

nb_address_N = 5
nb_address_p = 0.1

nb_purchase_mu = 5
nb_purchase_sigma = 2

cities = ['ottawa', 'edmonton', 'victoria', 'winnipeg', 'fredericton', 'st_john', 'halifax', 'toronto', 'charlottetown', 'quebec', 'regina', 'yellowknife', 'iqaluit', 'whitehorse']
guarantees = ['gmdb', 'gmwb']
genders = ['female', 'male']
funds = ['vanguard', 'fidelity', 'rowe', 'merril', 'morgan', 'barclays', 'sachs', 'paribas', 'fargo', 'suisse', 'citi', 'mizuho', 'lazard', 'evercore', 'nomura', 'jefferies']

seed(0)

if not exists(db_path) or force:
	print('making db ... ', end='')

	if exists(db_path):
		remove(db_path)

	db = sqlite3.connect(db_path)

	nb_client = int(nb_client)
	nb_guarantee = int(nb_guarantee)
	nb_fund_price = int(nb_fund_price)

	# client
	g = guarantees + list(','.join(g) for g in combinations(guarantees,2))
	client = pd.DataFrame(dict(
		cid = arange(nb_client)+1,
		city = choice(cities, nb_client),
		phone = randint(1e2, 1e3, nb_client),
		guarantee = choice(g, nb_client),
		gender = choice(genders, nb_client),
		date_of_birth = choice(pd.date_range('1970-01-01', '2000-01-01'), nb_client),
	))
	client.to_sql('client', db, index=False)

	# address
	address = pd.DataFrame()
	for cid in range(1, nb_client+1):
		n = binomial(nb_address_N, nb_address_p)

		x = pd.DataFrame(dict(	
			cid = [cid]*n,
			date = choice(pd.date_range('2016-01-01', '2018-01-01'), n),
			city = choice(cities, n),
			phone = randint(1e2, 1e3, n),
		))

		address = pd.concat([x, address])

	address = address.sample(frac=1)
	address.to_sql('address', db, index=False)

	# purchase
	purchase = pd.DataFrame()
	for cid in range(1, nb_client+1):
		n = int(normal(nb_purchase_mu, nb_purchase_sigma))
		n = max(randint(3), n)

		x = pd.DataFrame(dict(	
			cid = [cid]*n,
			date = choice(pd.date_range('2016-01-01', '2018-01-01'), n),
			amount = uniform(0, 1e4, n),
			fund = choice(funds, n),
		))

		purchase = pd.concat([x, purchase])

	purchase = purchase.sample(frac=1)
	purchase.to_sql('purchase', db, index=False)

	# guarantee
	init = pd.DataFrame(dict(	
		guarantee = guarantees,
		date = pd.to_datetime(['2016-01-01']*len(guarantees)),
		fee = uniform(0, 0.1, len(guarantees)),
	))

	after = pd.DataFrame(dict(	
		guarantee = choice(guarantees, nb_guarantee),
		date = choice(pd.date_range('2016-01-01', '2018-01-01'), nb_guarantee),
		fee = uniform(0, 0.1, nb_guarantee),
	))

	end = pd.DataFrame(dict(	
		guarantee = guarantees,
		date = pd.to_datetime(['2018-01-01']*len(guarantees)),
		fee = uniform(0, 0.1, len(guarantees)),
	))


	guarantee = pd.concat([init, after, end])

	guarantee.to_sql('guarantee_cost', db, index=False)

	# fund
	init = pd.DataFrame(dict(
		fund = funds,
		date = pd.to_datetime(['2016-01-01']*len(funds)),
		price = uniform(0, 1e2, len(funds)),
	))

	nb_fund = int(nb_client*2)
	after = pd.DataFrame(dict(	
		fund = choice(funds, nb_fund),
		date = choice(pd.date_range('2016-01-01', '2018-01-01'), nb_fund),
		price = uniform(0, 1e2, nb_fund),
	))

	end = pd.DataFrame(dict(
		fund = funds,
		date = pd.to_datetime(['2018-01-01']*len(funds)),
		price = uniform(0, 1e2, len(funds)),
	))

	fund = pd.concat([init, after, end])

	fund = fund.sample(frac=1)
	fund.to_sql('fund_price', db, index=False)

	print('db made')