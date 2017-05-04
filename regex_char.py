import re

char=raw_input("Enter the characters: ")
char_match=re.search('^[a-zA-Z]+$',char)
if char_match: 
	print "Its a character"
else:
	print "Its not a character"