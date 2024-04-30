x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc1():
    global y
    y = "excellent"
    print("Python is " + y)

myfunc1()

print("Python is " + y)
