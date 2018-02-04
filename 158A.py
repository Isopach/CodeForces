n,k = map(int,raw_input().split())
a = raw_input().split()
a1 = [int(i) for i in a]
count = 0
for i in a1:
    if((i>0)and(i>=a1[k-1])):
        count += 1
print count
"""if (a1[k] != 0) and (a1[k] == a1[k+1]):
    print len(a[0:k+1])+1
elif (a1[k] != 0) and (a1[k] != a1[k+1]):
    print len(a[0:k])+1
else:
    print 0"""