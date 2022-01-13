FirstNum = int(input("Enter Your First Number\n"))
SecondNum= int(input("Enter Your Second Number\n"))

def Compare (FirstNum,SecondNum):
    if FirstNum <= SecondNum:
        return FirstNum
    else:
        return SecondNum

print("The Minimum Number is: ",Compare(FirstNum,SecondNum))