#     Handling missing keys in Python dictionaries

myDict={101:"Ashutosh",102:"Shivam",103:"Java",104:"Cat",105:"jet"}

search= int(input("Enter Your Number\n"))

# for rollnum,name in myDict.items():
#     if rollnum == search:
#         print("Your Name is: ",name)
#         break
    
#     else:
#         print("Does not Exist")
#         # break

def Check(rollnum):
    for k in myDict:
        if k == rollnum:
            print (f"Your Name is: {myDict[k]}" )
            return myDict[k]
        else:
            continue

    return "Does Not exist"

print(Check(search))
   