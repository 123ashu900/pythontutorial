# num = int(input("Enter The Number"))
# fact= 1

# for i in range (1 , num+1):
#     fact=fact*i
# print(fact)


def greeting(name):
    print(f"hiii   {name}")
    print("\nhow are you\n")
def sum(num1,num2):
    sum=num1+num2
    return sum,"hiii"

studentName = input("enter your name\n")
# greeting(studentName)


sumresult,gret= sum(23,34)

print(sumresult,gret)