# annuity package

shows how to create a python package

# directory structure	

the directory structure must be

	root folder
		setup.py
		annuity_package
			__init__.py
			other_folders
			other_files.py


# how to create a package
	__init__.py: used to declare what to import from a folder
	
	setup.py: used to install a package
		a package can be think as a top-level folder

# installation
in cmder
	chdir package_root_folder
	python setup.py develop

# test/example	
To see if the package works, and for usage examples, see
	test_annuity_factor.py
