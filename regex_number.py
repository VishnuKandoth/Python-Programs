import re

numbr=raw_input("Enter numbers: ")
no_match=re.search('^\d+$',numbr)
if no_match: 
	print "Its Numeric Value"
else:
	print "Its a Non-Numeric value"