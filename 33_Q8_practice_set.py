#     Python | Reversing a List

from ast import Return
from audioop import reverse


mylist=[32,"Ashutosh",755,89.03,"react"]

newlist=[]
# mylist.reverse()
# print(mylist)

for x in range(len(mylist),0,-1):
    element=mylist[x-1]
    newlist.append(element)
print(newlist)