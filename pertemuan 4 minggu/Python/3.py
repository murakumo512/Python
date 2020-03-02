def total(x,y):
    x+=1
    y+=1
    x+=y
    return x,y

x = 10
y = 3

x,y = total(x,y)
print(x,y)