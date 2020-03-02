num1 = 13
num2 = 27
rep = 5
while rep > 0:
    if num2 > num1:
        num1 = num1 + num2
    else: 
        num2 = num2 + num1
    rep = rep -1
print(num1,num2)