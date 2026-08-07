"""

Question 10 – enumerate() (Index + Value)

Often we need both:
    -the position (index)
    -the actual value

Given:

    fruits = ["Apple", "Banana", "Mango", "Orange"]

Write a program that prints:

0 Apple
1 Banana
2 Mango
3 Orange

Requirements:
Use for loop.
Use enumerate().
Do not manually create an index variable.

"""

fruits = ["Apple", "Banana", "Mango", "Orange"]
for index,name in enumerate(fruits):
    print(f"{index} {name}")