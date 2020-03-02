a = 100
b = 17
while a > b:
    a = a - b
    if a % 2 ==0 :
        a = a + a % 2
print(a)