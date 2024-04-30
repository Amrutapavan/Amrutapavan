# Variables are to store data values and can be declared directly by assigning value to it
a = 5
x = "Amrutha"
print(a, x)

# Casting - if you want the specific data typeof a variable, this is done with casting
a = str(a)
a = int(a)
a = float(a)
print(a)
# Always any variable will take the last value assigned

# Get your type()
print(type(a))

# 'Single quote' or "Double quote" there will be no difference
x = 'Amrutha' #is same as
x = "Amrutha"


# Variables are case sensitive
y = 7
Y = "Pavan"
print(y,Y)

#Python Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple ", "strawberry ", "tomato"]
p, q, r =fruits
print(p)
print(q)
print(r)

print(p, q, r) # is same as
print(p + q + r)

# str + int causes error TypeError: unsupported operand type(s) for +: 'int' and 'str' but can be used with comma
