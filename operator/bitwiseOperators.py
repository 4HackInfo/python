#1 & 	AND	                    Sets each bit to 1 if both bits are 1	         = x & y
# |	    OR	                    Sets each bit to 1 if one of two bits is 1	     = x | y
# ^	    XOR	                    Sets each bit to 1 if only one of two bits is 1	 = x ^ y
# ~	    NOT	                    Inverts all the bits	                         = ~x
# <<	Zero fill left shift	Shift left by pushing zeros in from the right    = x << 2
#                               and let the leftmost bits fall off	

# >>	Signed right shift      Shift right by pushing copies of the             = x >> 2 
#                               leftmost bit in from the left, 
#                               and let the rightmost bits fall off



print(6 & 3) # 2 decimal , turn into binary calculation (&=* multiplication)

print(6 | 3) # 7 decimal , compares each bit and set it to 1 if one or both is 1