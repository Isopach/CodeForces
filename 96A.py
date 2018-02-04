import re
n = str(raw_input())
if re.search("0000000", n) or re.search("1111111", n):
    print "YES"
else:
    print "NO"