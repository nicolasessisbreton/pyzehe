# searching with ctrl+f

type ctrl+f
a search box appears below
click .* 
	this activates regex search

in the search box type
	search.*below
	press Enter
	type F3
	type shift+F3
		you circulate on the match
		this search box show the match as you type
		so its great to learn regex

# searching with / and regex
in move mode
	type /
	type search.*below
	press Enter
	type n
	type N
		you circulate on the match

# search and replace
	type ctrl+h

# moving over lines
in move mode
	type j
	type j
	type k
	type k
	type h
	type h
	type l
	type l

	type g 29 g
	type $
	type 0
	type $
	type 0

# selecting text
in move mode
	type g 46 g
	type v
	type l
	type l
	type j
	type j
	type k
	type h
		you can copy the selection with ctrl+c
		you can paste the selection with ctrl+v

# moving lines
in move mode
	type o
	type esc
	type O
	type esc
	type dd (delete)
	type p
	type P
	type yy (yank)
	type p
	type P

# moving over words
	type k
	type b
	type e
	type b
	type w
	type w
	type w
	type 0
	type f o
	type f o
	type f o
	type F o
	type F O

# moving selection
	select	
	these
	three lines
		type g 88 g
		type 0
		type v
		type jj
		type $

	type ctrl+[
	type ctrl+]
	type ctrl+]
	type ctrl+[

	type alt+up
	type alt+up
	type alt+down
	type alt+down
		(up is the 'up arrow' on your keyboard)
		(down is the 'down arrow' on your keyboard)
	
# inserting comment	
open test_all.py
	type gg v G
	type ctrl+/
	type ctrl+/
	