z = 10
def total(x,y,z):
    return x+y+z

x = 100
y = 5
z = 3

print(total(x,y,z))


def fun():
    print("a")
    fin()

def fin():
    return
    print("b")

fun()

def ancok(z):
    return lambda x,y: x*z/y

angka = ancok(6.5)
print(angka(6,5))


def ancoks(a,b):
    if(a>b):
        b+=1
        return b
    else:
        return ancuoks(b,a)

def ancuoks(a,b):
    a+=1
    return a
a = 3
b = 5
print(ancoks(a,b))

def asu(a,b,c):
    return pow(b,c,a)
print(asu(3,4,5))


def ado(a):
    return "iya" if doa(a) == 0 else "bukan"

def doa(a):
    return 0 if a%2 == 0 else 1
a = ado(3)
print(ado)