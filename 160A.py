n = int(raw_input())
m = raw_input().split()
a = [int (i) for i in m]

total = sum(a)
a = sorted(a, key=int)
tmp = []
while sum(tmp) <= total/2:
  tmp.append(a.pop())
  
print len(tmp)
