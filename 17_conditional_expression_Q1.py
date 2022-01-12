user=[]

user1= int(input("Enter Your Number: "))
user2= int(input("Enter Your Number: "))
user3= int(input("Enter Your Number: "))
user4= int(input("Enter Your Number: "))

user.append(user1)
user.append(user2)
user.append(user3)
user.append(user4)



if(user1>user4):
    a=user1
else:
    a=user4

if(user2<user3):
    b=user2
else:
    b=user3

user.sort()

print("The greater number is ",user.pop() )


