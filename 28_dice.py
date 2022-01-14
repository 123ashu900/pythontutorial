import random



while True:
    print("please throw\n")
    num=random.randint(1,6)

    if num<6:
        print("Your Number is: ",num)
        break
    else:
        print("Your Number is:",num,"Please Throw Again")
        
