name= ["Ashutosh","Saurav","Abhishek","Rohit","Mohan","Subham"]

search= input ("Enter Your Name\n")

if(search in name):
    print("Your {} is present in list".format(search))
else:
    print("{name} is not present in list".format(name=search))

