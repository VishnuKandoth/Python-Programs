import re 

spclchar=raw_input("Enter the Special Character: ")
spcl_match=re.search('^[&\\-()]+$',spclchar)
if spcl_match: 
	print "Its a special character"
else:
	print "Its not a special character"
