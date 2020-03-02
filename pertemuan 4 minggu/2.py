def fun(a):
    return "iya" if fin(a) == 0 else "bukan"

def fin(a):
    return 0 if a%2 == 0 else 1

a = fun(3)
print(a)


def zig(x):
    print("zag"*x,end='')
print("zig",end='')
def zag(x):
    print("zig"*x,end='')
    zig(x-1)

zig(2)
zag(2)