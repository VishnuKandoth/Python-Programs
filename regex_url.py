import re

url=raw_input("Enter the email: ")
urlid=re.compile("(^http[s]?://+[a-zA-Z0-9._]+.in$)")
match=urlid.match(url)
if match is None:
	print "URL not belong to India"
else:
	print "URL belong to India"


