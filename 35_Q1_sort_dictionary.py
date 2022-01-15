#     Python | Sort Python Dictionaries by Key or Value

oldDict={101:"Ashutosh",103:"Shivam",102:"Java",104:"Cat"}

list1=[]

newDict={}


for roll,name in oldDict.items():
    element=oldDict[roll]
    list1.append(roll)
    list1.sort()

for myroll  in list1:
    newDict[myroll]=oldDict[myroll]
    


   
print(newDict)


