mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String : %s" % mystring)

if isinstance(myfloat, float ) and myfloat == 10.0:
    print("float : %f" % myfloat)

if isinstance(myint, int) and myint == 20:
    print("integer : %d" % myint)

name = "riel"
age = 18
if name == "riel" and age == 18:
    print("your name is riel and your age is 23 years old!")

if name == "riel" or name == "rick":
    print("your name is either riel or rick")


name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")