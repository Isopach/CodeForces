n = int(raw_input())
count = 0
for i in range(0,n):
    a = map(int,raw_input().split())
    if sum(a) >= 2:
        count += 1
print count