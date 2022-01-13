#     Python – Swap elements in String list

fruits=["Mango","Banana","Grapes","Orange","Litchi"]

user1= int(input("Enter Your  1st Index number (0-4) to swap\n" ))
user2= int(input("Enter Your  1st Index number (0-4) to swap\n" ))

# def swapELement(index,index1,myfruits):
#     element1= myfruits[index]2
#     myfruits[index] = myfruits[index1]
#     myfruits[index1] = element1
#     return myfruits


# x=swapELement(1,3,fruits)
# print (x)

def swaplist(index1,index2,newlist):
    element= newlist[index1]
    newlist[index1] = newlist[index2]
    newlist[index2] = element
    return newlist

print(swaplist(user1,user2,fruits))
