def fun(a,b):
    if(a>b):
        b+=1
        return b
    else:
        return fin(b,a)

def fin(a,b):
    a+=1
    return a

a = 3
b = 5
print(fun(a,b))