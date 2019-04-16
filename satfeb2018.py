#!/usr/bin/python
import re

line="8=FIX.4.2;9=65;35=A;49=SERVER;56=CLIENT;34=177;52=20090107-18:15:16;98=0;108=30;10=062;"

pj=re.findall(r"^.*;56=.*$",line)
print pj
searchObj=re.search(r'^.*(8=FIX).*?;(9=.*?);(52=.*?).*$',line, re.I)
if searchObj:
  print "searchObj.group() : ", searchObj.group()
  print "searchObj.group(1) : ", searchObj.group(1)
  print "searchObj.group(2) : ", searchObj.group(2)
  print "searchObj.group(3) : ", searchObj.group(3)
else:
 print "No search!"

patterns = [ 'this', 'that' ]
text = 'Does this text match the pattern?'

for pattern in patterns:
    print 'Looking for "%s" in "%s" ->' % (pattern, text),

    if re.search(pattern,  text):
        print 'found a match!'
    else:
        print 'no match'
