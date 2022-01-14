Number =int(input("Enter Your Number\n"))


for triangle in range (Number,0,-1):
    for addspace in range(1,Number-triangle):
        print(" ",end="")
    for star in range(1,triangle+1):
            print("*", end=" ")    
    print("\n")


