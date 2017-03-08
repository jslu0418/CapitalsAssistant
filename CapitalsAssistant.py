import re

string = 'Capitalixation'
string = string.lower()
strlen = len(string)
regex = '^c' + '.' * (strlen - 2) + 'n$'
regexobj = re.compile(r''+regex)
result = regexobj.match(string)
if result:
    print result.group()
else:
    print 'No match'
