a = 1
b = (a*10+a)**2
for b in range (10):
    a = a + b
    b = b - a

print(a,b)