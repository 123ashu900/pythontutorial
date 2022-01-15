#     Python | Cloning or Copying a list

from turtle import clone


dict1={"101":{'Name':'Ashutosh','cls':'UG','rollnum':'1424'},
"102":{'Name':'Ashutosh','cls':'UG','rollnum':'1424'},
"103":{'Name':'Ashutosh','cls':'UG','rollnum':'1424'},
"104":{'Name':'Ashutosh','cls':'UG','rollnum':'1424'},
"105":{'Name':'Ashutosh','cls':'UG','rollnum':'1424'}}

list2= dict1



def cloning(dict1):
    copy_dict= dict1
    return copy_dict

print(cloning(dict1))
