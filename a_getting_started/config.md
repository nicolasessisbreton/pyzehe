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
we need to copy config files from the cmder folder to sublime folder

go to 
	Desktop\cmder\vendor\sublime\Data\Package
copy all the folder User

go to
	Desktop\sublime\Data\Packages\User
overwrite the User folder

in
	Desktop\sublime\Data\Packages\User
open 
	make_plugin.py
change the path of cmder_root at line 14
	cmder_root = dirname(dirname(sublime.executable_path()))
to the actual path
	cmder_root = r'C:\Users\nessisbr\Desktop\cmder'

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




