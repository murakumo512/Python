a = 17
b = 13
c = 10
for angka in range (10,0,-1):
    if a > c:
        a = a - b + c
    else:
        a = a - c + b

    print(a)
    