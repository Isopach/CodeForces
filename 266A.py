n = int(raw_input())
s = str(raw_input())
c = 0
for i in range(n-1):
    if s[i]==s[i+1]:
        c+=1
#if "RR" in s or "GG" in s or "BB" in s:
 #   c += 1
print c