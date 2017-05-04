import re

phone=raw_input("Enter the mobile number")
match1=re.search('[789]\d{9}$',phone)
if match1: 
	print "Phone_no is matching"
else:
	print "phone_no not matching "