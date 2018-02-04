n = raw_input()
n = n.lower()
m = raw_input()
m = m.lower()
value = dict()

no = []
mo = [] 
for character in n:
    number = ord(character) - 96
    no.append(number)

for character in m:
    number = ord(character) - 96
    mo.append(number)
#Self-note: Not sum, but just the number by itself.
if no > mo:
    print 1
elif mo > no:
    print -1
else:
    print 0