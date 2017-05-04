import re

data=raw_input("Enter the IP: ")
ip=re.search("^([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." +
		"([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." +
		"([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\." +
		"([01]?\\d\\d?|2[0-4]\\d|25[0-5])$",data)
if ip:
	print "IP Address Accepted"
else:
	print "IP Address Mismatching"
