#     Python program to interchange first and last elements in a list

myList1=[32,74,83,44,98]

# a= myList[0]
# myList[0]= myList[-1]

# myList[-1]= a


# print(myList)


def swaplist(index1,index2,mylist):
    element= mylist[index1]
    mylist[index1]= mylist[index2]
    mylist[index2]= element
    return mylist

p=0
q=4
x=swaplist(p,q,myList1)    
# print(swaplist(4,3,myList1))
print(x)

