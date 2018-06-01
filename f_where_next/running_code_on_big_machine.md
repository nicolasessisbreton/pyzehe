# speeding-up python
- python allows to write code fast
- speed is ok
- when speed is not ok, when can often get away with multiprocessing:
	- ex: laptop with 1 core, to blade with 100 cores: 100 times speed-up
	- ex: laptop with 1 core, 10 blades of 100 cores: 1000 times speed-up
	- one blade is 20K$
- python has libraries to make porting code to blades easy
	(multiprocessing and dask)

# excel machine
# classic vba
- for each row of a table, vba pushes inputs and outputs
- throwput of vba is 1 line/seconds
- there is 300K lines (5 days computations)

# excel machine
- throwput is usually 10 times faster (half day computation)

# excel machine on a blade of 60 cores
- throwput is 600 times faster
- can tackle table with 10 millions lines