print('hello')

print("Hello")

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)
print(x)

# string in array
y = "Hello World!"
print(y[1])
print(len(y))

# Looping Through a string
for c in "banana":
    print(c)

# Check if "free" is present in the following text
txt = "The best things in life are free!"
if "free" in txt:
    print("yes, 'free' is present.")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
print("expensive" not in txt)
# Use it in an if statement
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
