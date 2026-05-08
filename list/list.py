
"""

Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store 
collections of data, the other 3 are Tuple, Set, and Dictionary, 
all with different qualities and usage.

"""

# Lists are created using square brackets: ["",""]
thislist = ["apple", "banana", "cherry"]
print(thislist) #  ["apple", "banana", "cherry"]


# <1List Items> - access by index [1]
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # banana

# <List Length> - how many index inside the list
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # 3

# <The list() Constructor>
thislist = list(("banana","apple","orange"))
print(thislist)