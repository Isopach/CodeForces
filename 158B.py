n = int(raw_input())
s = [int(_) for _ in raw_input().split()]
c = 0
x = [0,0,0,0,0]
for i in s:
    x[i] += 1  
c = x[4]+x[3]
x[1]=max(x[1]-x[3],0)
c += (x[1]+x[2]*2+3)/4
"""
import re
import math
for four in re.findall("4", s):
    c += 1
for three in re.findall("3", s):
    c += 0.75
for two in re.findall("2", s):
    c += 0.5
for one in re.findall("1", s):
    c += 0.25"""
print c