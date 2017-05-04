import re

emailid=raw_input("Enter the email: ")
mailid=re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
idtest=mailid.match(emailid)
if idtest is None:
	print "mailid Mismatching"
else:
	print "mailid Accepted"