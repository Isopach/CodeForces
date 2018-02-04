n=raw_input()
if (n[0].islower() and n[1:].isupper()) or (len(n) == 1 and n.islower()):
    print str.capitalize(n)
elif n.isupper():
    print str.lower(n)
else:
    print n