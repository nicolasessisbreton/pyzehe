We need to configure python and sublime

# python config
open cmder.exe
type
	python -m pip install --upgrade pip --trusted-host pypi.org
	pip install --trusted-host pypi.org numpy scipy matplotlib pandas xlwings pillow pythonnet

we need to adjust comptype
	python C:\Apps\Python36\Tools\scripts\2to3.py -n -w -v C:\Apps\Python36\Lib\site-packages\comtypes

	(if your python is not located in: C:\Apps\Python36
	(type
	(		python -c "import sys; print(sys.executable)"
	(to find where it is


# sublime config
go to Desktop\sublime
click sublime_text.exe

we need to install package control, install a few packages and configure

## sublime: package control

google sublime package control
Installation

copy the line 'import urlib..write(by)'

go back to sublime
click View:Show Console
in the pane that opens: paste the line
press Enter

## sublime: packages
click Preferences:Package Control
type install package
press Enter
type vintageous
press Enter

## sublime: configure
#@ need to make this config folder

we need to copy config files from this tutorial to sublime folder

go to 
	Desktop\pyzehe\sublime_config
copy all the files in the folder

go to
	Desktop\sublime\DataPackages\User
paste all the files
overwrite any existing file if necessary


# what's next

you are all set now

begin your pyzehe journey 
by doing in sublime

	File:Open Folder
	choose Desktop\pyzehe
	type F11
	type ctrl+p
	type sublime.md
	press Enter




