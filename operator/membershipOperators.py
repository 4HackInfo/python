"""
Membership operators are used to test if a sequence is presented in an object:
"""

# in 	    Returns True if a sequence with the specified   = x in y	
#           value is present in the object	

# not in	Returns True if a sequence with the 
#           specified value is not present in the object	= x not in y


# Check if "banana" is present in a list:
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # True


# Check if "pineapple" is NOT present in a list:
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits) # True