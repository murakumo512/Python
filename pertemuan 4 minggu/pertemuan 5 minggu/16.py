def asu(a,b):
    if a < b:
        c = b + a
        return c
    else:
        c = a - b
        return c
c = asu(10,15)
for c in range(10):
    c = c+(c/2)+(c/3)

print(c)