a = 12
b = (a*10+a)**2
c = (b*2+a)%10
for b in range (10):
    a = a + b
    b = b - a
    c = c + a - b
print(a,b,c)