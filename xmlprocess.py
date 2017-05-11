from xml.dom import minidom
xmldoc = minidom.parse('sample.xml')
itemlist = xmldoc.getElementsByTagName('child')
print(len(itemlist))
print(itemlist[0].attributes['value'].value)
for s in itemlist:
   print(s.attributes['value'].value)

iteml = xmldoc.getElementsByTagName('parent')
for k in iteml:
   print(k.attributes['name'].value)
