#Integer DataType stores integer values. The int data type takes 28 Bytes out of which
#4 bytes are actual values
print("Integer DataType")
nAge = 25
nMarks = 90
print(nAge)
print(nMarks)

#Float DataType stores decimal values.
print("Float DataType")
fPrice = 23.34
fWeight = 45.67
print(fPrice)
print(fWeight)

#String stores the text data
print("String DataType")
strName = "Andrew"
strMessage = "Hello, How are you?"
print(strName)
print(strMessage)

#Boolean DataType stores True or False values.
print("Boolean DataType")
bIsStudent = True
bIsTeacher = False
print(bIsStudent)
print(bIsTeacher)

#List DataType stores multiple values in a single variable.
print("List DataType")
lstFruits = ["Apple", "Banana", "Cherry"]
lstNumbers = [1, 2, 3, 4, 5]
print(lstFruits)
print(lstNumbers)

#List DataType stores multiple datatypes as well
mixedList = [1, "Hello", 3.14, True]
print(mixedList)

#List is mutable, meaning you can change its content without changing its identity.
#This includes the index data type as well
mixedList[1] = "World"
mixedList[0] = "How are you?"
print(mixedList)

#Tuple DataType stores multiple values in a single variable. Tuples are immutable, meaning you cannot change its content without changing its identity.
print("Tuple DataType")
tplFruits = ("Apple", "Banana", "Cherry")
tplNumbers = (1, 2, 3, 4, 5)
print(tplFruits)
print(tplNumbers)

#Set Store unique values in a single variable. Sets are unordered, meaning the items do not have a defined order.
print("Set DataType")
setFruits = {"Apple", "Banana", "Cherry", "Banana", "Cherry"}
setNumbers = {1, 2, 3, 4, 5, 3, 4, 5}
print(setFruits)
print(setNumbers)

#Dictionary DataType stores key-value pairs in a single variable. Dictionaries are unordered, meaning the items do not have a defined order.
print("Dictionary DataType")
dictStudent = {"Name": "Andrew", "Age": 25, "Marks": 90}
dictTeacher = {"Name": "John", "Age": 35, "Subject": "Maths"}
print(dictStudent)
print(dictTeacher)
print(dictStudent["Name"])
print(dictTeacher["Subject"])

#type() function is used to get the data type of a variable.
print("Data Type of nAge is: ", type(nAge))
