import re
n = int(raw_input())
x = 0
for i in range(0,n):
    stm = raw_input()
    casematching = stm.replace("--X","-1").replace("X--","-1").replace("++X","1").replace("X++","1")
    x += int(casematching)
print x
    
    
