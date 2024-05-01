import random
print(random.randrange(1, 10))


x = 1       #int
y = 2.8     #float
z = 1j      #complex

print(type(x))
print(type(y))
print(type(z))

# for integer
a = 1
b = 352864511
c = -568425

# for float
d = 10.10
e = 1.0
f = -35.59

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100
print(y)
print(type(x))
print(type(y))
print(type(z))

# for complex

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Convert from one type to another

x = 1
y = 2.8
z = 1j

# convert from int to float:
p = float(x)
# convert from float to int:
q = int(y)
# convert from int to complex:
r = complex(x)

print(p)
print(q)
print(r)

print(type(p))
print(type(q))
print(type(r))
