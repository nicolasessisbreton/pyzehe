"""
here we produce visualization with excel

# one-time excel preparation
	in cmder
		xlwings addin install

	open excel
		enable Trust access to VBA 
			File > Options > Trust Center > Trust Center Settings > Macro Settings

# making the visualization workbook
	in cmder
		chdir this_directory
		xlwings quickstart book_report

	the result of this is in
		sol_book_report\*

# studying the visualization
	in cmder type excel
	open with excel sol_book_report\book_report.xlsm

	open with sublime book_report.py
"""