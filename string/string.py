
#1 <c>
print("hello world".capitalize()) # Hello world
print("hello".casefold())      # hello
print("hello".center(10, "-")) # --hello---
print("hello".count("l"))      # 2

############################################

# <e>
print("hello".encode())      # b'hello'
print("hello".endswith("o")) # True
print("a\tb".expandtabs(4))  # a   b

############################################

# <f>

print("hello {}".format("world"))  # hello world
print("hello".find("l"))           # 2

#############################################

# <i> - used for checking condition

print("123".isalnum())          # True
print("abc".isalpha())          # True
print("hello".isascii())        # True
print("123".isdecimal())        # True
print("123".isdigit())          # True
print("hello".islower())        # True
print("hello".isprintable())    # True
print("   ".isspace())          # True
print("Hello World".istitle())  # True
print("HELLO".isupper())        # True

#############################################

# <j>
print("-".join(["a", "b", "c"]))  # a-b-c


#############################################

# <L>

print("hello".ljust(10, "-"))  # hello-----
print("hello".lower())         # hello
print("   hello".lstrip())     # hello

##############################################

# <m>
print("hello".maketrans("h", "H"))  # {104: 72}

##############################################

# <p>
print("hello world".partition(" "))  # ('hello', ' ', 'world')

##############################################

# <r>
print("hello".replace("l", "x"))  # hexxo
print("hello".rfind("l"))         # 3
print("hello world".rpartition(" "))  # ('hello', ' ', 'world')
print("hello".rjust(10, "-"))     # -----hello
print("   hello   ".rstrip())     #    hello

##############################################

# <s>
print("hello world".split())   # ['hello', 'world']
print("a\nb".splitlines())     # ['a', 'b']
print("hello".startswith("h")) # True
print("   hello   ".strip())   # hello
print("HELLO".swapcase())      # HELLO

###############################################

# <t>
print("hello world".title())                       # Hello World
print("hello".translate(str.maketrans("h", "H")))  # Hello

###############################################

# <u>
print("hello".upper())  # HELLO

###############################################

# <z>
print("42".zfill(5))  # 00042