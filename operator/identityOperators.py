

"""
Identity operators are used to compare the objects, not if they are equal, 
but if they are actually the same object, with the same memory location:
"""

#1 is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)