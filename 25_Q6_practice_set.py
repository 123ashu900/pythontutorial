FirstNum = float(input("Enter Your First Number\n"))
SecondNum = float(input("Enter Your Second Number\n"))
ThirdNum = float(input("Enter Your Third Number\n"))

def Biggest (a,b,c):
    if a>=b and a>=c:
        print ("The Biggest Number is: " , a)
    elif b>=a and b>=c:
        print("The Biggest Number is: ", b)
    else:
        print("The Biggest Number is: ", c)

Biggest(FirstNum,SecondNum,ThirdNum)    