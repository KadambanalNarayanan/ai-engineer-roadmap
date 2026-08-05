"""
Write a Python program 
1. Create these variables
country = "India"
population = 1400000000
growth_rate = 0.8
is_developed = False

2. Print the value and its data type for each variable
The output should look like below

India <class 'str'>
1400000000 <class 'int'>
0.8 <class 'float'>
False <class 'bool'>

Requirements
    -Use the type() function.
    -Use one print() statement for each variable.
    -Don't use loops yet.
"""

country = "India"
population = 1400000000
growth_rate = 0.8
is_developed = False

print(f"{country} {type(country)}")
print(f"{population} {type(population)}")
print(f"{growth_rate} {type(growth_rate)}")
print(f"{is_developed} {type(is_developed)}")