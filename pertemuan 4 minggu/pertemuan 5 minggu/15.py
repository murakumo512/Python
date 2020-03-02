def zig(x):
    print("Zag"*x,end='')
print("Zig",end='')
def zag(x):
    print("Zig"*x,end='')
    zig(x-1)
zig(2)
zag(2)