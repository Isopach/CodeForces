import re
string = str(raw_input())
casematching = string.replace("A","").replace("E","").replace("I","").replace("O","").replace("U","").replace("a","").replace("e","").replace("i","").replace("o","").replace("u","").replace("Y","").replace("y","")
newstr = ""
tmp = ["." + i for i in casematching]
case= ''.join(i for i in tmp)
for ul in case:
    if ul.isupper():
        newstr += ul.lower()
    else:
        newstr += ul.lower()
print newstr