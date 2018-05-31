code executes linearly, but is written non-linearly

sublime is the perfect non-linear editor

To use this power, we need to learn a few commands

# navigating between files

type ctrl+p
type the name of the file you want

the name can
	sublime.md (full name)
	subl (partial name)
	s u md (partial name)

when the same file exists in many folder 
you can prefix the name with the name of the folder
	a get subl (for: a_getting_started/sublime.md)
	a test all (for: a_getting_started/test_all.py
	b test all (for: b_basic/test_all.py

# navigation in a file

open sublime.md
	type ctrl+p
	type sublime.md
	press enter

	type ctrl+r
		you will see a list of header

open syntax.py 
	type ctrl+p
	type syntax.py
	press enter

	type ctrl+r
		you will see a list of functions

# moving the cursor
open sublime.md
	
when the cursor blinks: you are in move mode			
when the cursor is a line: you are in edit mode 

to switch between the two
	move mode --type i--> edit mode
	edit mode --type esc--> move mode

in move mode 
	type gg (you go to the top)
	type G (you go to the end)
	type g 51 g (you go to line 51)

	type /
		type moving 
		press Enter
		type n
		type N
			you circulate on moving

# want to know more?

look at moves.md
	type ctrl+p
	type moves.md 
	press enter

# what's next
open test_all.py
	type ctrl+p
	type a test all
	press enter

look at the topics
	you see that the next topic is exercise.md

open exercise.md
	ctrl+p
	type a exercise
	press enter
