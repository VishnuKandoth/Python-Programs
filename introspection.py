import sys
def fun():
	pass

class test:
   def intro(self):
      pass

class test2:
   def fun():
      pass


t = test()

print " "
print "Dir: "
print dir(t)
print dir([])

print " "
print "Type: "
print type([])
print type({})

print "  "
print "Id: " 
print id([])
print id(sys)
print id(t.intro)

print " "
print "Callable: "
print callable(t.intro)

print " "
print "IsInstance: "
print isinstance(t,test)
print isinstance(t,test2)