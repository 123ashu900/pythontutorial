myDict = {"khidki":"Window",
"ghar":"House",
"billi":"cat",
"hathi":"Elephant" }

print("Please select", myDict.keys() )

a= input("Enter the Hindi word\n")

print("Meaning of these word in enlish is:", myDict.get(a))
