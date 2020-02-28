import random
import math
import numbers

x = 21
def fun():
    x = 19
    x -=1
    def fin():
        global x
        if x%2!=0:
            x +=1
        else:
            x-=1
    fin()
fun()
print("x : ",x )