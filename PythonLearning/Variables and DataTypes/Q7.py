"""

Without running the code, predict the output.

import copy

list1 = [[1, 2], [3, 4]]

list2 = copy.deepcopy(list1)

list2[0].append(100)

print(list1)
print(list2)

print(list1 is list2)
print(list1 == list2)


print(list1)
print(list2)
list1 is list2
list1 == list2
Explain why deepcopy() behaves differently from .copy().


Ans: Normal coy do not copy inner list however deep copy copy inner list as well

"""