n = int(raw_input())
cap =0
maxx = []
for i in range(0,n):
    a,b = map(int,raw_input().split())
    cap -= a
    cap += b
    maxx.append(cap)
    #print cap
print max(maxx)