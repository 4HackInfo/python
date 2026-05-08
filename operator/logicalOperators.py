
# and : 1x1 = True  (both True or 1) 
# or = 1+1 = True  (either 1 or 0)
#  not = !1  = False (Reverse True or false)


# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

#1 <and>
x = 5
print(x > 0 and x < 10) # True

# <or>
x = 5
print(x < 5 or x > 10) # True

# <not>
x = 5
print(not(x > 3 and x < 10)) # False 

