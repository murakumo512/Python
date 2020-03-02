def fun():
    x = 20
    def fin():
        x = 30
        print('x =',x)
    print('x = ', x)
    fin()

x = 10
fun()
print('x =',x)